package com.dbank.speedup.upload;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;
import java.util.zip.CRC32;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import sun.net.www.protocol.http.HttpURLConnection;

/**
 * <�?��话功能简�?
 * <功能详细描述>
 *
 * @author c57771
 * @version [版本�? 13-9-26]
 * @see  [相关�?方法]
 * @since [产品/模块版本]
 */
public class HuaweiDbankCloud
{
    private static final Log log = LogFactory.getLog(DefaultHostProvider.class);

    private static final String USER_AGENT = "SPEEDUP-UPLOAD-SDK 1.0.O";

    private static final int UPLOAD_STATUS_NEED_ALL = 2;

    private static final int UPLOAD_STATUS_NEED_PARTIAL = 1;

    private static final int SEGMENT_SIZE = 5 * 1024 * 1024;
//    private static int SEGMENT_SIZE = 256;

    private static final int SAMPLING_SIZE = 1024 * 1024 + 1;

    private static String DBANK_API_HOST = "api.dbank.com";

    private String appId;

    private String appName;

    private String secret;

    private int maxRetryTimes = 4;

    private HostProvider hostProvider;


    public HuaweiDbankCloud(String appId, String appName, String secret)
    {
        this.appId = appId;
        this.appName = appName;
        this.secret = secret;
        this.hostProvider = new DefaultHostProvider();
    }

    public void upload(String path, File file, String callbackUrl, String callbackStatus) throws IOException
    {
        if (path == null || path.charAt(0) != '/' || path.charAt(path.length() - 1) == '/')
        {
            throw new IllegalArgumentException("invalid path." + path);
        }
        if (file == null || file.length() == 0)
        {
            throw new IllegalArgumentException("invalid file.");
        }
        String host = getUploadHost();
        long fileLength = file.length();
        String fileMd5 = Utils.getFileMd5(file, 0, file.length());
        String contentMd5 = getContentMd5(fileMd5, file);

        long offset = doInit(path, callbackUrl, callbackStatus, host, fileLength, fileMd5, contentMd5);
        //已经飞�?�?
        if (offset == -1)
        {
            log.info("hit fast upload.");
            return;
        }
        int retryTimes = 0;
        while (true)
        {
            if (offset == -1)
            {
                break;
            }
            long length = fileLength - offset;
            if (length > SEGMENT_SIZE)
            {
                length = SEGMENT_SIZE;
            }
            //已经传完�?
            if (length <= 0)
            {
                break;
            }
            if (log.isInfoEnabled())
            {
                log.info("upload file=" + file.getAbsoluteFile() + ",offset=" + offset + ",length=" + length);
            }
            try
            {
                offset = doUpload(path, file, callbackUrl, callbackStatus, host, fileLength, fileMd5, contentMd5, offset, (int)length);
            }
            catch (IOException e)
            {
                log.error("upload failed.", e);
                retryTimes++;
            }
            if (retryTimes > maxRetryTimes)
            {
                break;
            }
        }
        log.info("upload completed");
    }

    public void upload(String path, File file, String host,String callbackUrl, String callbackStatus) throws IOException
    {
        if (path == null || path.charAt(0) != '/' || path.charAt(path.length() - 1) == '/')
        {
            throw new IllegalArgumentException("invalid path." + path);
        }
        if (file == null || file.length() == 0)
        {
            throw new IllegalArgumentException("invalid file.");
        }
        //String host = getUploadHost();
        long fileLength = file.length();
        String fileMd5 = Utils.getFileMd5(file, 0, file.length());
        String contentMd5 = getContentMd5(fileMd5, file);

        long offset = doInit(path, callbackUrl, callbackStatus, host, fileLength, fileMd5, contentMd5);
        //已经飞�?�?
        if (offset == -1)
        {
            log.info("hit fast upload.");
            return;
        }
        int retryTimes = 0;
        while (true)
        {
            if (offset == -1)
            {
                break;
            }
            long length = fileLength - offset;
            if (length > SEGMENT_SIZE)
            {
                length = SEGMENT_SIZE;
            }
            //已经传完�?
            if (length <= 0)
            {
                break;
            }
            if (log.isInfoEnabled())
            {
                log.info("upload file=" + file.getAbsoluteFile() + ",offset=" + offset + ",length=" + length);
            }
            try
            {
                offset = doUpload(path, file, callbackUrl, callbackStatus, host, fileLength, fileMd5, contentMd5, offset, (int)length);
            }
            catch (IOException e)
            {
                log.error("upload failed.", e);
                retryTimes++;
            }
            if (retryTimes > maxRetryTimes)
            {
                break;
            }
        }
        log.info("upload completed");
    }
    private long doUpload(String path, final File file, String callbackUrl, String callbackStatus, String host, long fileLength, String fileMd5, String contentMd5, final long offset, final int length) throws IOException
    {
        TreeMap<String, String> headers = buildCommonHeaders(fileMd5, contentMd5, fileLength, callbackUrl, callbackStatus);
        headers.put("nsp-content-range", String.valueOf(offset).concat("-").concat(String.valueOf(offset + length - 1)).concat("/").concat(String.valueOf(fileLength)));
        buildSig(path, headers);
        return Utils.httpPut("http://".concat(host).concat(path), headers, new Utils.Callback<Long>()
        {
            @Override
            void callback(OutputStream out) throws IOException
            {
                Utils.copyFile(file, offset, length, out);
            }

            @Override
            protected Long callback(int code, InputStream body) throws IOException
            {
                String content = Utils.toString(body);
                if (log.isDebugEnabled())
                {
                    log.debug("upload:http code=" + code + ",body=" + content);
                }
                //全部上传好了
                if (code == HttpURLConnection.HTTP_OK)
                {
                    return -1l;
                }
                if (code != HttpURLConnection.HTTP_CREATED)
                {
                    throw new IOException("unknown http code for upload,code=" + code);
                }
                UploadStatus status = Utils.toObject(content, UploadStatus.class);
                if (UPLOAD_STATUS_NEED_PARTIAL == status.getUpload_status())
                {
                    return status.getCompleted_range()[0][1];
                }
                else
                {
                    return 0l;
                }
            }
        });

    }

    private long doInit(String path, String callbackUrl, String callbackStatus, String host, long fileLength, String fileMd5, String contentMd5) throws IOException
    {
        String initPath = path.concat("?init");
        //String initPath = path;
        TreeMap<String, String> initHeaders = buildCommonHeaders(fileMd5, contentMd5, fileLength, callbackUrl, callbackStatus);
        buildSig(initPath, initHeaders);
        return Utils.httpPut("http://".concat(host).concat(initPath), initHeaders, new Utils.Callback<Long>()
        {
            @Override
            public Long callback(int code, InputStream body) throws IOException
            {
                String content = Utils.toString(body);
                if (log.isDebugEnabled())
                {
                    log.debug("init:http code=" + code + ",body=" + content);
                }
                //全部上传好了
                if (code == HttpURLConnection.HTTP_OK)
                {
                    return -1l;
                }
                if (code != HttpURLConnection.HTTP_CREATED)
                {
                    throw new IOException("unknown http code for init upload,code=" + code);
                }
                UploadStatus status = Utils.toObject(content, UploadStatus.class);
                if (UPLOAD_STATUS_NEED_PARTIAL == status.getUpload_status())
                {
                    return status.getCompleted_range()[0][1];
                }
                else
                {
                    return 0l;
                }
            }
        });
    }

    private void buildSig(String path, TreeMap<String, String> headers) throws UnsupportedEncodingException
    {
        StringBuilder params = new StringBuilder();
        for (Map.Entry<String, String> entry : headers.entrySet())
        {
            params.append(entry.getKey())
                    .append('=')
                    .append(entry.getValue())
                    .append('&');
        }
        params.deleteCharAt(params.length() - 1);
        String tempSecret = Utils.hashMac(headers.get("nsp-ts"), secret);
        StringBuilder encryptSource = new StringBuilder(128);
        encryptSource.append("PUT")
                .append('&')
                .append(URLEncoder.encode(path, Utils.ENCODING))
                .append('&')
                .append(URLEncoder.encode(params.toString(), Utils.ENCODING));
        String nspSig = Utils.base64HashMac(encryptSource.toString(), tempSecret);

        headers.put("nsp-sig", nspSig);
        headers.put("Expect", "100-continue");
    }

    private TreeMap<String, String> buildCommonHeaders(String fileMd5, String contentMd5, long fileLength, String callbackUrl, String callbackStatus)
    {
        TreeMap<String, String> headers = new TreeMap<String, String>();
        headers.put("nsp-ts", String.valueOf(System.currentTimeMillis() / 1000));
        headers.put("nsp-file-md5", fileMd5);
        headers.put("nsp-file-size", String.valueOf(fileLength));
        headers.put("nsp-content-md5", contentMd5);
        if (callbackUrl != null && callbackStatus != null)
        {
            headers.put("nsp-callback", callbackUrl);
            headers.put("nsp-callback-status", callbackStatus);
        }
        return headers;
    }

    private String getContentMd5(String fileMd5, File file) throws IOException
    {
        long fileLength = file.length();
        String[] md5s = new String[2];
        for (int i = 1; i <= 2; i++)
        {
            CRC32 crc32 = new CRC32();
            crc32.update((fileMd5 + i).getBytes());
            long offset = crc32.getValue() % fileLength;
            long length = SAMPLING_SIZE;
            if (fileLength - offset < length)
            {
                length = fileLength - offset;
            }
            if (log.isDebugEnabled())
            {
                log.debug("content md5 range:offset=" + offset + ",length=" + length);
            }
            md5s[i - 1] = Utils.getFileMd5(file, offset, length).toLowerCase();
        }


        return Utils.toJsonString(md5s);
    }

    private String getUploadHost() throws IOException
    {
        Map<String, String> params = new HashMap<String, String>();
        params.put("rip", "");
        return hostProvider.getUploadHost(appId, secret, params);
    }

    public void setMaxRetryTimes(int maxRetryTimes)
    {
        this.maxRetryTimes = maxRetryTimes;
    }

    public static void main(String[] args) throws IOException
    {
//        System.setProperty("http.proxyHost", "127.0.0.1");
//        System.setProperty("http.proxyPort", "8888");
      //  HuaweiDbankCloud huaweiDbankCloud = new HuaweiDbankCloud("60850", "xqd", "yuaHJ4GEaoCXGIV2WRgWlGsvROhITUIg");
        //HuaweiDbankCloud huaweiDbankCloud = new HuaweiDbankCloud("59826", "phoneService", "tdaho5d0ba5h6g6d97xv1q4lxb6iw8c0");
        HuaweiDbankCloud huaweiDbankCloud = new HuaweiDbankCloud("50985", "TDS", "test50985bba8df90acb8eb160a8087f");
        //        huaweiDbankCloud.upload("/dl/TDS/abc/test2.dat", new File("C:\\Users\\c57771\\soft"), null, null);
        String callback="http://210.21.230.170:8081/osg/logServerAction!uf.htm?lsId=08da7032-5147-4080-a2fb-0047440b468a&st=G8TEAq18giKhcvzDUv4ZIbXB2QUcPv9UMq8dqDlY9yI%3D";
        String callbackStatus="200";
        huaweiDbankCloud.upload("/dlv2/TDS/hwdevlogbeta/logtest/test.zip", new File("D:\\test.zip"), "upload.dbank.com",callback, callbackStatus);
    }
}
