package com.huawei.cloudplus.test;

import java.io.File;

import nsp.NSPClient;

import com.dbank.speedup.upload.HuaweiDbankCloud;
import com.huawei.autospace.tools.*;
import com.huawei.autospace.util.*;
import com.huawei.cloud.file.AbsUploadHelper;
import com.huawei.cloudplus.test.bean.FileMeta;
import com.huawei.cloudplus.test.bean.PingOption;
import com.huawei.cloudplus.test.bean.PingRet;

public class DBankTester extends ActionWord{

	public int dlmkfile(){
		logReport(Log.LL_DEBUG, "Begin to execute \"dlmkfile\" function.");
		// parse and get AW parameters
		String strappid = getParaValue("nsp_app");
		String strsecret = getParaValue("secret");
		String strURL = getParaValue("URL");
		String strbucket = getParaValue("bucket");
		String strpath = getParaValue("path");
		String strfid = getParaValue("fid");
		String strurl = getParaValue("url");
		String strfilename = getParaValue("filename");
		String strresult = getParaValue("result");
		
		/*
		strappid = "59826";
		strsecret = "tdaho5d0ba5h6g6d97xv1q4lxb6iw8c0";
		strbucket ="hwdevlogbeta";
		strpath = "/test";
		strfid = "85a8bd3fdd6198b4f8bef9fd032e512d";
		strurl = "http://test/zz.zip";
		strfilename = "zz.zip";
*/

		String reslut = "";

		try {
			
			 NSPClient nspClient = new NSPClient(Integer.valueOf(strappid),strsecret);
			 
			 nspClient.callService("nsp.dl.mkfile",new Object[]{strbucket,strpath,strfilename,strfid,strurl},String.class);
			 reslut="OK";
			
			
		} catch (Exception e) {

			reslut = e.getMessage();
		}

		this.addOutputPara("result", reslut);
		//System.out.println(reslut);


		return RESULT_OK;
	}
	
	


	/*************************************************************************
	* AW name      :    dlgetfile
	* description  :    
	* input        :    sUri            : AW URI
	*                   sParameter      : a string includes some AW parameters
	* output       :    result          : AW running result
	* return       :    if successful, the return value is zero, otherwise it is nonzero
	*
	* AW parameters:   
	*                   nsp_app         : 
	*                   secret          : 
	*                   bucket          : 
	*                   path            : 父文件夹路径。
	*                   filename        : 
	*                   result          : 
	*************************************************************************/
	public int dlgetfile(){
		logReport(Log.LL_DEBUG, "Begin to execute \"dlgetfile\" function.");
		// parse and get AW parameters
		String strnsp_app = getParaValue("nsp_app");
		String strsecret = getParaValue("secret");
		String strbucket = getParaValue("bucket");
		String strpath = getParaValue("path");
		String strfilename = getParaValue("filename");
		String strresult = getParaValue("result");

/*
		strnsp_app = "59826";
		strsecret = "tdaho5d0ba5h6g6d97xv1q4lxb6iw8c0";
		strbucket ="hwdevlogbeta";
		strpath = "/test";
		strfilename = "test22.zip";
	*/	
		String reslut = "";

		try {
			
			 NSPClient nspClient = new NSPClient(Integer.valueOf(strnsp_app),strsecret);
			 
			
			FileMeta fm= nspClient.callService("nsp.dl.getFile",new Object[]{strbucket,strpath,strfilename},FileMeta.class);
			if(null!=fm){
			 reslut="filename:"+fm.getFilename()+";";
			 reslut=reslut+"fid:"+fm.getFid()+";";
			 reslut=reslut+"bucket:"+fm.getBucket()+";";
			 reslut=reslut+"path:"+fm.getPath()+";";
			 reslut=reslut+"url:"+fm.getUrl();
			}else{
				reslut="no record";
			}
			
		} catch (Exception e) {
			e.printStackTrace();
			reslut = e.getMessage();
		}

		this.addOutputPara("result", reslut);
		//System.out.println(reslut);


		return RESULT_OK;

	}

	/*************************************************************************
	* AW name      :    dlrmFile
	* description  :    
	* input        :    sUri            : AW URI
	*                   sParameter      : a string includes some AW parameters
	* output       :    result          : AW running result
	* return       :    if successful, the return value is zero, otherwise it is nonzero
	*
	* AW parameters:   
	*                   nsp_app         : 
	*                   secret          : 
	*                   fid             : 
	*                   result          : 
	*************************************************************************/
	public int dlrmFile(){
		logReport(Log.LL_DEBUG, "Begin to execute \"dlrmFile\" function.");
		// parse and get AW parameters
		String strnsp_app = getParaValue("nsp_app");
		String strsecret = getParaValue("secret");
		String strfid = getParaValue("fid");
		String strresult = getParaValue("result");

		String reslut = "";
		//strnsp_app = "59826";
		//strsecret = "tdaho5d0ba5h6g6d97xv1q4lxb6iw8c0";
		//strfid = "85a8bd3fdd6198b4f811403573077539";
		
		try {
			
			 NSPClient nspClient = new NSPClient(Integer.valueOf(strnsp_app),strsecret);
			 
			 nspClient.callService("nsp.dl.rmFile",new Object[]{strfid},String.class);
			 reslut="OK";
			
			
		} catch (Exception e) {
			e.printStackTrace();
			reslut = e.getMessage();
		}

		this.addOutputPara("result", reslut);
		//System.out.println(reslut);


		return RESULT_OK;
	}
	
	


	/*************************************************************************
	* AW name      :    dlmarkDelete
	* description  :    
	* input        :    sUri            : AW URI
	*                   sParameter      : a string includes some AW parameters
	* output       :    result          : AW running result
	* return       :    if successful, the return value is zero, otherwise it is nonzero
	*
	* AW parameters:   
	*                   nsp_app         : 
	*                   secret          : 
	*                   bucket          : 
	*                   path            : 父文件夹路径。
	*                   files           : 可传入多个文件名，以“;”隔开
	*                   result          : 
	*************************************************************************/
	public int dlmarkDelete(){
		logReport(Log.LL_DEBUG, "Begin to execute \"dlmarkDelete\" function.");
		// parse and get AW parameters
		String strnsp_app = getParaValue("nsp_app");
		String strsecret = getParaValue("secret");
		String strbucket = getParaValue("bucket");
		String strpath = getParaValue("path");
		String strfiles = getParaValue("files");
		String strresult = getParaValue("result");
		
		//strnsp_app = "59826";
		//strsecret = "tdaho5d0ba5h6g6d97xv1q4lxb6iw8c0";
		//strbucket ="hwdevlogbeta";
		//strpath = "/local";
		//strfiles = null;

		String reslut = "";
		String[] fs=null;
		if(null!=strfiles&&!strfiles.equalsIgnoreCase("")){
			fs=strfiles.split(";");
		}

		try {
			
			 NSPClient nspClient = new NSPClient(Integer.valueOf(strnsp_app),strsecret);
			 
			 nspClient.callService("nsp.dl.markDelete",new Object[]{strbucket,strpath,fs},String.class);
			 reslut="OK";
			
			
		} catch (Exception e) {
			e.printStackTrace();
			reslut = e.getMessage();
		}

		this.addOutputPara("result", reslut);
		//System.out.println(reslut);


		return RESULT_OK;
	}

	/*************************************************************************
	* AW name      :    dlgetDeletedList
	* description  :    
	* input        :    sUri            : AW URI
	*                   sParameter      : a string includes some AW parameters
	* output       :    result          : AW running result
	* return       :    if successful, the return value is zero, otherwise it is nonzero
	*
	* AW parameters:   
	*                   nsp_app         : 
	*                   secret          : 
	*                   result          : 
	*************************************************************************/
	public int dlgetDeletedList(){
		logReport(Log.LL_DEBUG, "Begin to execute \"dlgetDeletedList\" function.");
		// parse and get AW parameters
		String strnsp_app = getParaValue("nsp_app");
		String strsecret = getParaValue("secret");
		String strresult = getParaValue("result");
		String reslut = "";

		//strnsp_app = "59826";
		//strsecret = "tdaho5d0ba5h6g6d97xv1q4lxb6iw8c0";

		try {
			
			 NSPClient nspClient = new NSPClient(Integer.valueOf(strnsp_app),strsecret);
			 
			 String[] fids=nspClient.callService("nsp.dl.getDeletedList",null,String[].class);
			 if(null!=fids&&fids.length>0){
				 for(int i=0;i<fids.length;i++){
					 reslut=reslut+fids[i]+";";
				 }
				 reslut=reslut.substring(0, reslut.length()-1);
			 }else{
				 reslut="no record";
			 }
			 
			
			
		} catch (Exception e) {
			e.printStackTrace();
			reslut = e.getMessage();
		}

		this.addOutputPara("result", reslut);
		//System.out.println(reslut);

		return RESULT_OK;


	}

	
	public static void main(String[] args) {

		try {

			new DBankTester().dlgetDeletedList();

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	/*************************************************************************
	* AW name      :    pingGetupsrvip
	* description  :    
	* input        :    sUri            : AW URI
	*                   sParameter      : a string includes some AW parameters
	* output       :    result          : AW running result
	* return       :    if successful, the return value is zero, otherwise it is nonzero
	*
	* AW parameters:   
	*                   nsp_app         : 
	*                   secret          : 
	*                   client_ip       : 
	*                   vip_level       : 
	*                   result          : 
	*************************************************************************/
	public int pingGetupsrvip(){
		logReport(Log.LL_DEBUG, "Begin to execute \"pingGetupsrvip\" function.");
		// parse and get AW parameters
		String strnsp_app = getParaValue("nsp_app");
		String strsecret = getParaValue("secret");
		String strclient_ip = getParaValue("client_ip");
		String strvip_level = getParaValue("vip_level");
		String strresult = getParaValue("result");
		/*
		strnsp_app = "59826";
		strsecret = "tdaho5d0ba5h6g6d97xv1q4lxb6iw8c0";
		strclient_ip="10.46.31.2";
		strvip_level="95";
		*/
		String reslut="";
		try {
			PingOption po=new PingOption();
			po.setVip_level(strvip_level);
			
			 NSPClient nspClient = new NSPClient(Integer.valueOf(strnsp_app),strsecret);
			 
			 PingRet pr=nspClient.callService("nsp.ping.getupsrvip",new Object[]{strclient_ip,po},PingRet.class);
			 reslut="isSucc:"+String.valueOf(pr.isSucc())+";IP:"+pr.getIp();
			
			
		} catch (Exception e) {

			reslut = e.getMessage();
		}

		this.addOutputPara("result", reslut);
		//System.out.println(reslut);

		return RESULT_OK;

	}
	
	public int uploadLog(){
		logReport(Log.LL_DEBUG, "Begin to execute \"pingGetupsrvip\" function.");
		// parse and get AW parameters
		String strnsp_app = getParaValue("nsp_app");
		String strsecret = getParaValue("secret");
		String strclient_ip = getParaValue("client_ip");
		String strvip_level = getParaValue("vip_level");
		String strresult = getParaValue("result");
		/*
		strnsp_app = "59826";
		strsecret = "tdaho5d0ba5h6g6d97xv1q4lxb6iw8c0";
		strclient_ip="10.46.31.2";
		strvip_level="95";
		*/
		String reslut="";
		try {
			
			
			 NSPClient nspClient = new NSPClient(Integer.valueOf(strnsp_app),strsecret);
			// nspClient.uploadFile(host, tstr, file)
			 
			
			
		} catch (Exception e) {

			reslut = e.getMessage();
		}

		this.addOutputPara("result", reslut);
		//System.out.println(reslut);

		return RESULT_OK;

	}
	

	/*************************************************************************
	* AW name      :    dluplogfile
	* description  :    
	* input        :    sUri            : AW URI
	*                   sParameter      : a string includes some AW parameters
	* output       :    result          : AW running result
	* return       :    if successful, the return value is zero, otherwise it is nonzero
	*
	* AW parameters:   
	*                   nsp_app         : 
	*                   secret          : 
	*                   ip              : 
	*                   uploadurl       : 
	*                   filename        : 
	*                   localpath       : 文件本地所在路径
	*                   url             : 
	*                   result          : 
	*************************************************************************/
	public int dluplogfile(){
		logReport(Log.LL_DEBUG, "Begin to execute \"dluplogfile\" function.");
		// parse and get AW parameters
		String strnsp_app = getParaValue("nsp_app");
		String appname = getParaValue("appname");
		String strsecret = getParaValue("secret");
		String strip = getParaValue("ip");
		String strdluplogfile = getParaValue("dluplogfile");
		String strfilename = getParaValue("filename");
		String strlocalpath = getParaValue("localpath");
		String strurl = getParaValue("url");
		String strresult = getParaValue("result");


		String reslut="";
		try {
			
	        HuaweiDbankCloud huaweiDbankCloud = new HuaweiDbankCloud(strnsp_app, appname, strsecret);
	        //String callback="http://210.21.230.170:8081/osg/logServerAction!uf.htm?lsId=08da7032-5147-4080-a2fb-0047440b468a&st=G8TEAq18giKhcvzDUv4ZIbXB2QUcPv9UMq8dqDlY9yI%3D";
	        String callback="http://192.168.195.126/lvs/";
	        String callbackStatus="200";
	        huaweiDbankCloud.upload(strdluplogfile, new File(strlocalpath), strip,callback, callbackStatus);
			 
	        reslut="OK";
			
		} catch (Exception e) {

			reslut = e.getMessage();
		}

		this.addOutputPara("result", reslut);
		//System.out.println(reslut);

		return RESULT_OK;
	}

	/*************************************************************************
	* AW name      :    pinggetsrvip
	* description  :    
	* input        :    sUri            : AW URI
	*                   sParameter      : a string includes some AW parameters
	* output       :    result          : AW running result
	* return       :    if successful, the return value is zero, otherwise it is nonzero
	*
	* AW parameters:   
	*                   nsp_app         : 
	*                   secret          : 
	*                   client_ip       : 
	*                   vip_level       : 
	*                   result          : 
	*************************************************************************/
	public int pinggetsrvip(){
		logReport(Log.LL_DEBUG, "Begin to execute \"pinggetsrvip\" function.");
		// parse and get AW parameters
		String strnsp_app = getParaValue("nsp_app");
		String strsecret = getParaValue("secret");
		String strclient_ip = getParaValue("client_ip");
		String strvip_level = getParaValue("vip_level");
		String strresult = getParaValue("result");

		
		//strnsp_app = "59826";
		//strsecret = "tdaho5d0ba5h6g6d97xv1q4lxb6iw8c0";
		//strclient_ip="10.46.31.2";
		//strvip_level="95";
		
		String reslut="";
		try {
			PingOption po=new PingOption();
			po.setVip_level(strvip_level);
			
			 NSPClient nspClient = new NSPClient(Integer.valueOf(strnsp_app),strsecret);
			 
			 PingRet pr=nspClient.callService("nsp.ping.getsrvip",new Object[]{strclient_ip,po},PingRet.class);
			 reslut="isSucc:"+String.valueOf(pr.isSucc())+";IP:"+pr.getIp();
			
			
		} catch (Exception e) {

			reslut = e.getMessage();
		}

		this.addOutputPara("result", reslut);
		//System.out.println(reslut);

		return RESULT_OK;
	}
	
	public int uploadtest(){
		
		return 0;
	}

}
