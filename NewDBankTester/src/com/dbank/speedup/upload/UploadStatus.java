package com.dbank.speedup.upload;

/**
 * <�?��话功能简�?
 * <功能详细描述>
 *
 * @author c57771
 * @version [版本�? 13-10-8]
 * @see  [相关�?方法]
 * @since [产品/模块版本]
 */
public class UploadStatus
{
    private int upload_status;

    private long[][] completed_range;

    public int getUpload_status()
    {
        return upload_status;
    }

    public void setUpload_status(int upload_status)
    {
        this.upload_status = upload_status;
    }

    public long[][] getCompleted_range()
    {
        return completed_range;
    }

    public void setCompleted_range(long[][] completed_range)
    {
        this.completed_range = completed_range;
    }
}
