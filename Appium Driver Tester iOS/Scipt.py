from appium import webdriver
import time

def initialize_appium_driver():
    """
    Initializes the Appium driver with predefined desired capabilities.

    Returns:
        webdriver.Remote: The Appium driver instance if successful.
    """
    # Replace these variables with your actual device and Appium server details
    UDID = "00008030-001235042107802E"  # Replace with your device's UDID
    XCODE_ORG_ID = "9VG3A52D8L"  # Replace with your actual Xcode Organization ID
    WDA_BUNDLE_ID = "your.bundle.id.WebDriverAgentRunner"  # Replace with your WDA bundle ID
    APP_BUNDLE_ID = "com.apple.Preferences"  # Example: Settings app. Replace with your target app's bundle ID if needed.

    desired_caps = {
        "xcodeOrgId": XCODE_ORG_ID,  # Your actual Xcode Org ID
        "xcodeSigningId": "iPhone Developer",  # Typically "iPhone Developer"
        "platformName": "iOS",
        "automationName": "XCUITest",
        "udid": UDID,  # Unique Device Identifier of your iOS device
        "deviceName": "iPhone",  # Can be any name, e.g., "iPhone 12"
        "bundleId": APP_BUNDLE_ID,  # Bundle ID of the app you want to test
        "updatedWDABundleID": WDA_BUNDLE_ID,  # Bundle ID for WebDriverAgent
        "showXcodeLog": True,
        "newCommandTimeout": 300,  # Timeout in seconds
        "useNewWDA": True,
        "noReset": True  # Don't reset app state between sessions
    }

    appium_server_url = "http://localhost:4723/wd/hub"  # Default Appium server URL and port

    while True:
        try:
            driver = webdriver.Remote(appium_server_url, desired_caps)
            print("Appium server started and connected successfully.")
            print(f"Session ID: {driver.session_id}")
            return driver
        except Exception as e:
            print(f"Failed to connect to Appium server: {e}")
            print("Retrying in 2 seconds...")
            time.sleep(2)

def main():
    """
    Main function to initialize the Appium driver and perform a simple test.
    """
    driver = initialize_appium_driver()

    try:
        # Perform a simple action: open the specified app and verify it's active
        driver.activate_app("com.apple.Preferences")  # Example: Activating the Settings app
        time.sleep(3)  # Wait for the app to open

        # Retrieve and print the current app's state
        app_state = driver.query_app_state("com.apple.Preferences")
        print(f"App State for 'com.apple.Preferences': {app_state}")

    finally:
        # Always quit the driver session
        driver.quit()
        print("Appium driver session ended.")

if __name__ == "__main__":
    main()
