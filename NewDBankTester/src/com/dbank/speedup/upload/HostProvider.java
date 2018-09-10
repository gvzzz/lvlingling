package com.dbank.speedup.upload;

import java.io.IOException;
import java.util.Map;

/**
 * <�?��话功能简�?
 * <功能详细描述>
 *
 * @author c57771
 * @version [版本�? 13-9-29]
 * @see  [相关�?方法]
 * @since [产品/模块版本]
 */
public interface HostProvider
{
    /**
     * 获取�?��上传服务器的地址
     * @return ip地址
     */
    String getUploadHost(String appId,String secret, Map<String, String> params) throws IOException;
}
