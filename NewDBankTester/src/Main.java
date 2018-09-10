import java.util.Date;

import com.huawei.autospace.tools.Log;
import com.huawei.autospace.util.*;

public class Main extends ActionWord implements AWInterface{
	/**
	 * Register AW interfaces and this will be called for the first time 
	 * when this package is loaded.
	 * @return 0-success, other-failed
	 */
	public int RegisterImpl() {
		return 0;
	}
	/**
	 * Unregister AW interfaces
	 * @return 0-successful, other-failed
	 */
	public int UnRegisterImpl() {
		return 0;
	}
	/**
	 * Initialize the environment and this will be called by 
	 * AutoSpace every time before executing a case.
	 * @return result of initialization
	 */
	public int InitEnv() {
		return 0;
	}
	/**
	 * Uninitialize the environment and this will be called by 
	 * AutoSpace every time after executing a case.
	 * @return result of clearing up
	 */
	public int ClearEnv() {
		return 0;
	}
	 
public static void main(String[] args){
		
	Date date =new Date("Thu, 01-Jan-1970 00:00:01 GMT");
	System.out.print(date.getTime());
		
	}
   
	
}
