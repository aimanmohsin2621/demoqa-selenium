def capture_network_logs(driver):
    """
    Capture network requests (HAR simulation).
    """
    logs = driver.get_log("performance")
    for log in logs:
        print(log)
