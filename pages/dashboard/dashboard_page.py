from playwright.sync_api import Page

from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.students_char_view = ChartViewComponent(page, 'students', 'bar')
        self.activities_char_view = ChartViewComponent(page, 'activities', 'line')
        self.courses_char_view = ChartViewComponent(page, 'courses', 'pie')
        self.scores_char_view = ChartViewComponent(page, 'scores', 'scatter')
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)

    def check_visible_students_chart(self):
        self.students_char_view.check_visible('Students')

    def check_visible_activities_chart(self):
        self.activities_char_view.check_visible('Activities')

    def check_visible_courses_chart(self):
        self.courses_char_view.check_visible('Courses')

    def check_visible_scores_chart(self):
        self.scores_char_view.check_visible('Scores')
