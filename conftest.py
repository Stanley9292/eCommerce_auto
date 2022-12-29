import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    request.cls.driver = driver
    yield
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if 'init_driver' in item.fixturenames else False
            if is_frontend_test:
                results_dir = os.environ.get("RESULTS_DIR", 'screenshots')
                if not results_dir:
                    raise Exception("Environment variable 'RESULTS_DIR' must be set.")
                screenshot_name = os.path.join(results_dir, item.name + '.png')
                driver_fixture = item.funcargs['request']
                driver_fixture.cls.driver.save_screenshot(screenshot_name)
                extra.append(pytest_html.extras.image(screenshot_name))
                
        report.extra = extra

