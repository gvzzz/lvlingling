report_url = "http://shark.ymmoa.com/api/show/status"    #查报告的url
report_header = {"ymmoa_user": '{%22name%22:%22%E6%9D%8E%E4%BD%B3%E7%BE%8E%22%2C%22avatarUrl%22:%22%22%2C%22departmentName%22:%22%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83%22%2C%22id%22:10236%2C%22jobNumber%22:%22Y0010236%22}'} #查报告的header
trigger_url = "http://shark.ymmoa.com/api/run/runSuiteASync"   #触发构建的url
trigger_header = {"Content-Type": 'application/json', "ymmoa_user": '{%22name%22:%22%E6%9D%8E%E4%BD%B3%E7%BE%8E%22%2C%22avatarUrl%22:%22%22%2C%22departmentName%22:%22%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83%22%2C%22id%22:10236%2C%22jobNumber%22:%22Y0010236%22}'} #触发构建的header
trigger_header