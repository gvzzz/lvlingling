package com.dbank.speedup.upload;

import java.io.IOException;
import java.util.Map;

/**
 * <ä¸?¥è¯åè½ç®è¿?
 * <åè½è¯¦ç»æè¿°>
 *
 * @author c57771
 * @version [çæ¬å? 13-9-29]
 * @see  [ç¸å³ç±?æ¹æ³]
 * @since [äº§å/æ¨¡åçæ¬]
 */
public interface HostProvider
{
    /**
     * è·åæ?½³ä¸ä¼ æå¡å¨çå°å
     * @return ipå°å
     */
    String getUploadHost(String appId,String secret, Map<String, String> params) throws IOException;
}
