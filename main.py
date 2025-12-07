from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty
from kivymd.theming import ThemeManager
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivy_garden.mapview import MapView, MapMarker, MapLayer
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivymd.toast import toast
import datetime
from kivy.graphics import Color, Line

Window.size = (360, 640)

LabelBase.register(
    name="OpenSans-VariableFont_wdth,wght",
    fn_regular="OpenSans-VariableFont_wdth,wght.ttf",
    fn_bold="OpenSans-Bold.ttf",
)

KV = """
MainWindow:
    id: manager
    LoginScreen:
        id: login
    SignupScreen:
    HomeScreen:
    ProfileScreen:
    ScheduleScreen:
    MapScreen:
    InboxScreen:
    PersonalInfoScreen:

<LoginScreen>
    name: "login"
    mobile_num: m_number
    password: password

    FloatLayout:
        FitImage:
            source: "login_bg.jpg"
        Image:
            source: "logo.png"
            size_hint: None, None
            size: "180dp", "180dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.86}

        MDLabel:
            text: "Log in"
            bold: True
            font_name: "OpenSans-VariableFont_wdth,wght"
            halign: "left"
            font_size: "22sp"
            valign: "center"
            size_hint: None, None
            pos_hint: {"x": 0.1, "top": 0.73}

        BoxLayout:
            orientation: "vertical"
            size_hint: 0.9, None
            height: self.minimum_height
            pos_hint: {"center_x": 0.5, "center_y": 0.43}
            padding: "20dp"
            spacing: "15dp"

            MDTextField:
                id: m_number
                hint_text: "Enter Student ID"
                font_name: "OpenSans-VariableFont_wdth,wght"
                font_size: "12sp"
                height: "50dp"
                mode: "rectangle"
                multiline: False
                pos_hint: {"center_x": 0.5}
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1

            MDTextField:
                id: password
                hint_text: "Enter password"
                password: True
                font_name: "OpenSans-VariableFont_wdth,wght"
                font_size: "12sp"
                mode: "rectangle"
                pos_hint: {"center_x": 0.5}
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1

            MDRectangleFlatButton:
                text: "Login"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: root.login_inter()

            MDRectangleFlatButton:
                text: "Signup"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "signup"

<SignupScreen>
    name: "signup"
    create_num: c_number
    c_pass: c_pass
    v_pass: v_pass

    FloatLayout:
        FitImage:
            source: "signup_bg.jpg"
        MDLabel:
            text: "Sign in"
            bold: True
            font_name: "OpenSans-VariableFont_wdth,wght"
            halign: "left"
            font_size: "22sp"
            valign: "center"
            size_hint: None, None
            pos_hint: {"x": 0.1, "top": 0.73}
        Image:
            source: "logo.png"
            size_hint: None, None
            size: "180dp", "180dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.86}
        BoxLayout:
            orientation: "vertical"
            size_hint: 0.9, None
            height: self.minimum_height
            pos_hint: {"center_x": 0.5, "center_y": 0.38}
            padding: "20dp"
            spacing: "15dp"
            MDTextField:
                id: c_number
                hint_text: "Create mobile number"
                size_hint_x: None
                mode: "rectangle"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1
            MDTextField:
                id: c_pass
                hint_text: "Create password"
                password: True
                mode: "rectangle"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                size_hint_x: None
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1
            MDTextField:
                id: v_pass
                hint_text: "Verify your password"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                password: True
                mode: "rectangle"
                size_hint_x: None
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1
            MDRectangleFlatButton:
                text: "Signup"
                size_hint_x: 1
                height: "55dp"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                text_color: "black"
                on_release: root.signup_inter()
            MDRectangleFlatButton:
                text: "Back"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: root.go_back()

<HomeScreen>:
    name: "homepage"

    canvas.before:
        Color:
            rgba: 0.05, 0.06, 0.1, 1 
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"

        ScrollView:
            do_scroll_x: False

            BoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height
                width: root.width

                MDLabel:
                    id: welcome_label
                    text: "Welcome, User!"
                    halign: "center"
                    font_style: "H5"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    bold: True
                    size_hint_y: None
                    height: dp(40)

                GridLayout:
                    cols: 1
                    spacing: "20dp"
                    size_hint_y: None
                    height: self.minimum_height

                    MDCard:
                        size_hint: None, None
                        size: root.width - dp(40), dp(80)  
                        elevation: 6
                        padding: "20dp"
                        radius: [15,]
                        md_bg_color: get_color_from_hex("#1F2937")
                        on_release: app.on_profile()

                        BoxLayout:
                            orientation: "vertical"
                            spacing: "5dp"

                            BoxLayout:
                                orientation: "horizontal"
                                spacing: "5dp"

                                MDLabel:
                                    text: "Profile"
                                    valign: "center"
                                    font_style: "H6"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_y": 0.5}
                                    height: "40dp"

                            MDLabel:
                                text: "View and edit your profile information."
                                font_style: "Body2"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size_hint_y: None
                                height: "20dp"
                                halign: "left"


                    MDCard:
                        size_hint: None, None
                        size: root.width - dp(40), dp(80)
                        elevation: 6
                        padding: "20dp"
                        radius: [15,]
                        md_bg_color: get_color_from_hex("#1F2937")
                        on_release: app.on_schedule()

                        BoxLayout:
                            orientation: "vertical"
                            spacing: "5dp"

                            BoxLayout:
                                orientation: "horizontal"
                                spacing: "5dp"

                                MDLabel:
                                    text: "Schedule"
                                    valign: "center"
                                    font_style: "H6"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_y": 0.5}
                                    height: "40dp"

                            MDLabel:
                                text: "View and manage your daily events."
                                font_style: "Body2"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size_hint_y: None
                                height: "20dp"
                                halign: "left"

                    MDCard:
                        size_hint: None, None
                        size: root.width - dp(40), dp(80)
                        elevation: 6
                        padding: "20dp"
                        radius: [15,]
                        md_bg_color: get_color_from_hex("#1F2937")
                        on_release: app.on_map()

                        BoxLayout:
                            orientation: "vertical"
                            spacing: "5dp"

                            BoxLayout:
                                orientation: "horizontal"
                                spacing: "5dp"

                                MDLabel:
                                    text: "Map"
                                    valign: "center"
                                    font_style: "H6"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_y": 0.5}
                                    height: "40dp"

                            MDLabel:
                                text: "Locate places and navigate easily."
                                font_style: "Body2"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size_hint_y: None
                                height: "20dp"
                                halign: "left"

                MDLabel:
                    text: "Pathfinding System"
                    font_style: "H5"
                    bold: True
                    halign: "left"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    padding_y: "10dp"
                    size_hint_y: None
                    height: dp(35)

                MDLabel:
                    text: "An intelligent campus navigation support system that guides users through a structured digital map. It interprets campus layout data to display connected campus paths between key locations such as academic buildings, offices, facilities, and landmarks. The system helps users better understand campus structure, explore possible directions, and recognize access points through clear visual path markers on the map."
                    font_style: "Caption"
                    halign: "left"
                    theme_text_color: "Custom"
                    text_color: 0.85, 0.85, 0.9, 1
                    size_hint_y: None
                    text_size: root.width - dp(40), None
                    max_lines: 8
                    shorten: False
                    height: dp(90)  


<ProfileScreen>:
    name: "profile"

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size    

    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height        
        padding: "10dp"
        spacing: "10dp"
        pos_hint: {"top": 0.88}
        width: self.parent.width
        size_hint_x: 1

        OneLineListItem:
            text: "Personal Info"
            on_release: app.root.current = "information"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1

        OneLineListItem:
            text: "Logout"
            on_release: app.root.current = "login"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1


    MDTopAppBar:
        title: "Profile"
        pos_hint: {"top": 1}
        md_bg_color: get_color_from_hex("#0A0D14")
        specific_text_color: 1, 1, 1, 1
        elevation: 0

    BoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: 0.10, 0.13, 0.20, 1
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

<PersonalInfoScreen>:
    name: "information"

    canvas.before:
        Color:
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size

    ScrollView:
        do_scroll_x: False

        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: self.minimum_height
            padding: "20dp"
            spacing: "14dp"
            width: root.width

            MDLabel:
                text: "Personal Information"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                halign: "center"
                font_style: "H6"
                size_hint_y: None
                height: dp(20)

            BoxLayout:
                orientation: "horizontal"
                spacing: "12dp"
                size_hint_y: None
                height: dp(60)

                MDTextField:
                    id: last_name
                    hint_text: "First Name"
                    halign: "left"
                    mode: "rectangle"
                    size_hint_x: 0.5
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDTextField:
                    id: first_name
                    hint_text: "Last Name"
                    halign: "left"
                    mode: "rectangle"
                    size_hint_x: 0.5
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

            MDLabel:
                text: "Course"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                halign: "left"
                font_style: "H6"
                size_hint_y: None
                height: dp(24)

            MDTextField:
                id: course
                hint_text: "Course"
                mode: "rectangle"
                text_color_normal: 1, 1, 1, 1
                text_color_focus: 1, 1, 1, 1
                hint_text_color_normal: 0.7, 0.7, 0.7, 1
                hint_text_color_focus: 1, 1, 1, 1
                max_lines: 2
                shorten: True
                shorten_from: "right"

            MDLabel:
                text: "Section"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                halign: "left"
                font_style: "H6"
                size_hint_y: None
                height: dp(24)

            MDTextField:
                id: section
                hint_text: "Section"
                mode: "rectangle"
                text_color_normal: 1, 1, 1, 1
                text_color_focus: 1, 1, 1, 1
                hint_text_color_normal: 0.7, 0.7, 0.7, 1
                hint_text_color_focus: 1, 1, 1, 1
                max_lines: 1
                shorten: True
                shorten_from: "right"

            MDLabel:
                text: "Year"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                halign: "left"
                font_style: "H6"
                size_hint_y: None
                height: dp(24)

            MDTextField:
                id: year
                hint_text: "Year (e.g., 2nd Year)"
                mode: "rectangle"
                text_color_normal: 1, 1, 1, 1
                text_color_focus: 1, 1, 1, 1
                hint_text_color_normal: 0.7, 0.7, 0.7, 1
                hint_text_color_focus: 1, 1, 1, 1
                max_lines: 1
                shorten: True
                shorten_from: "right"

            Widget:
                size_hint_y: None
                height: dp(10)  # small bottom spacing

    BoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: 0.10, 0.13, 0.20, 1
        padding: "10dp"

        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

<ScheduleScreen>:
    name: "schedule"
    subject: subject
    room: room
    day: day
    time_start: time_s
    time_end: time_e
    table_box: table_box

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Class Schedule"
            md_bg_color: get_color_from_hex("#0A0D14")
            specific_text_color: 1, 1, 1, 1
            elevation: 0

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "15dp"
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "Schedule Details"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "H6"
                    halign: "center"
                    size_hint_y: None
                    height: dp(30)

                MDLabel:
                    text: "Subject"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body1"
                    halign: "left"
                    size_hint_y: None
                    height: dp(20)

                MDTextField:
                    id: subject
                    hint_text: "Enter Subject"
                    mode: "rectangle"
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDLabel:
                    text: "Building"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body1"
                    halign: "left"
                    size_hint_y: None
                    height: dp(20)

                MDTextField:
                    id: building
                    hint_text: "Select Building"
                    mode: "rectangle"
                    on_focus: if self.focus: root.building_picker()
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDLabel:
                    text: "Room"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body1"
                    halign: "left"
                    size_hint_y: None
                    height: dp(20)

                MDTextField:
                    id: room
                    hint_text: "Select Room"
                    readonly: True
                    mode: "rectangle"
                    on_focus: if self.focus: root.room_picker()
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDLabel:
                    text: "Day"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body1"
                    halign: "left"
                    size_hint_y: None
                    height: dp(20)

                MDTextField:
                    id: day
                    hint_text: "Select Day"
                    readonly: True
                    mode: "rectangle"
                    on_focus: if self.focus: root.day_picker()
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDBoxLayout:
                    spacing: "10dp"
                    size_hint_y: None
                    height: dp(60)

                    MDTextField:
                        id: time_s
                        hint_text: "Start Time"
                        readonly: True
                        mode: "rectangle"
                        on_focus: if self.focus: root.show_start_time()
                        text_color_normal: 1, 1, 1, 1
                        text_color_focus: 1, 1, 1, 1
                        line_color_normal: 1, 1, 1, 1
                        line_color_focus: 1, 1, 1, 1
                        hint_text_color_normal: 0.7, 0.7, 0.7, 1
                        hint_text_color_focus: 1, 1, 1, 1

                    MDTextField:
                        id: time_e
                        hint_text: "End Time"
                        readonly: True
                        mode: "rectangle"
                        on_focus: if self.focus: root.show_end_time()
                        text_color_normal: 1, 1, 1, 1
                        text_color_focus: 1, 1, 1, 1
                        line_color_normal: 1, 1, 1, 1
                        line_color_focus: 1, 1, 1, 1
                        hint_text_color_normal: 0.7, 0.7, 0.7, 1
                        hint_text_color_focus: 1, 1, 1, 1

                MDRaisedButton:
                    text: "Add Schedule"
                    md_bg_color: get_color_from_hex("#81C784")
                    pos_hint: {"center_x": 0.5}
                    on_release: root.add_schedule()

                MDLabel:
                    text: "Your Schedule"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    halign: "center"
                    font_style: "Subtitle1"
                    padding_y: "10dp"

                MDBoxLayout:
                    id: table_box
                    orientation: "vertical"
                    size_hint_y: None
                    height: dp(300)

    MDBoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: get_color_from_hex("#0A0D14")
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1     


<MapScreen>:
    name: "map"

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size     

    MapView:
        id: mapview
        lat: 16.93804
        lon: 121.76454
        zoom: 18  

    MDTopAppBar:
        id: toolbar  # <-- add this
        title: "Map"
        pos_hint: {"top": 1}
        md_bg_color: get_color_from_hex("#0A0D14")
        specific_text_color: 1, 1, 1, 1
        elevation: 0
        left_action_items: [["menu", lambda x: root.open_menu()]]

    MDBoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: get_color_from_hex("#0A0D14")
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1 


<InboxScreen>:
    name: "inbox"

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size    

    MDTopAppBar:
        title: "Inbox"
        pos_hint: {"top": 1}
        md_bg_color: get_color_from_hex("#0A0D14")
        specific_text_color: 1, 1, 1, 1
        elevation: 0


    BoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: 0.10, 0.13, 0.20, 1
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
"""

VALID_ROOMS = {
    "Ramon Magsaysay Building": {

        "rooms": {"1st Floor": ["RM101", "RM102", "RM103"],
                  "2nd Floor": ["Abbreviation Room"]
                  },
        "coords": (16.937715315657673, 121.76392437370077)
    },
    "CCSICT Building": {
        "rooms": {"1st Floor": ["IT101", "IT102", "IT103", "IT104"],
                  "2nd Floor": ["IT201", "IT202", "IT203", "IT204"],
                  "3rd Floor": ["IT301", "IT302", "IT303", "IT304"]
                  },
        "coords": (16.938197528772875, 121.764063538908)
    },
    "CBM Building": {
        "rooms": {"2nd Floor": ["NB101"],
                  "3rd Floor": ["NB201"],
                  "4th Floor": ["NB301"]
                  },
        "coords": (16.936043364524572, 121.76446658242533)
    },
    "CED Building": {
        "rooms": {"1st Floor": ["UBA", "UBB", "OB101", "OB201"]
                  },
        "coords": (16.937139129220466, 121.76490974482596)
    },
    "SAS Building": {
        "rooms": {"1st Floor": ["SAS101", "SAS201"]
                  },
        "coords": (16.93736905890547, 121.76374652183607)
    },
}

Main_buildings = {
    "Ramon Magsaysay": (16.937715315657673, 121.76392437370077),
    "CCSICT Building": (16.938197528772875, 121.764063538908),
    "CBM Building": (16.936043364524572, 121.76446658242533),
    "CED Building": (16.937139129220466, 121.76490974482596),
    "SAS Building": (16.93736905890547, 121.76374652183607),
}

INTERSECTIONS = {
    "Int1_guardpost": (16.935905, 121.764017),
    "Int2_administrationB": (16.936217, 121.764092),
    "Int3_inside_building_left": (16.936343, 121.763921),
    "int4_volly_court": (16.936759, 121.764020),
    "Int5_left_road": (16.936779, 121.763883),
    "int6_left_road_to_chapel": (16.936138, 121.763760),
    "int6_front_sas": (16.937271, 121.763996),
    "Int7_front_magsaysay": (16.937844, 121.764130),
    "Int8_front_ccsict_near_gym": (16.938324, 121.764229),
    "Int9_front_poly_room": (16.938213, 121.764876),
    "Int10_front_educ_faculty": (16.937747, 121.764766),
    "Int11_front_cbm": (16.937077, 121.764618),
    "Int12_front_educ_elem": (16.936674, 121.764519),
    "Int13_basketball_court": (16.936697, 121.764414),
    "Int14_inside_building_right": (16.936220, 121.764259),
    "Int15_front_cbm_building": (16.936017, 121.764347),
    "front_of_ccscit_midman": (16.938095, 121.764178),
    "front_of_magsaysay_midman": (16.937580, 121.764060),
}

NODES = {**Main_buildings, **INTERSECTIONS}

GRAPH = {
    "Int1_guardpost": {
        "Int2_administrationB": 36,
        "int6_left_road_to_chapel": 38,
        "Int15_front_cbm_building": 38

    },
    "Int2_administrationB": {
        "Int1_guardpost": 36,
        "Int3_inside_building_left": 23,
        "Int14_inside_building_right": 19
    },
    "Int3_inside_building_left": {
        "Int2_administrationB": 23,
        "int4_volly_court": 47,

    },
    "Int14_inside_building_right": {
        "Int2_administrationB": 19,
        "Int13_basketball_court": 55
    },
    "int4_volly_court": {
        "Int3_inside_building_left": 47,
        "Int5_left_road": 18
    },
    "Int5_left_road": {
        "int4_volly_court": 18,
        "int6_left_road_to_chapel": 72,
        "int6_front_sas": 56
    },
    "int6_left_road_to_chapel": {
        "Int1_guardpost": 38,
        "Int5_left_road": 72
    },
    "int6_front_sas": {
        "Int5_left_road": 56,
        "Int11_front_cbm": 73,
        "front_of_magsaysay_midman": 35,
        "SAS Building": 6,
    },
    "SAS Building": {
        "int6_front_sas": 6
    },
    "front_of_magsaysay_midman": {
        "Int7_front_magsaysay": 33,
        "int6_front_sas": 35,
        "Ramon Magsaysay": 12
    },
    "Ramon Magsaysay": {
        "front_of_magsaysay_midman": 12
    },
    "Int7_front_magsaysay": {
        "front_of_magsaysay_midman": 33,
        "front_of_ccscit_midman": 29,
        "Int10_front_educ_faculty": 70
    },
    "front_of_ccscit_midman": {
        "Int7_front_magsaysay": 33,
        "Int8_front_ccsict_near_gym": 26,
        "CCSICT Building": 9
    },
    "CCSICT Building": {
        "front_of_ccscit_midman": 9
    },
    "Int8_front_ccsict_near_gym": {
        "front_of_ccscit_midman": 26,
        "Int9_front_poly_room": 74
    },
    "Int9_front_poly_room": {
        "Int8_front_ccsict_near_gym": 74,
        "Int10_front_educ_faculty": 53
    },
    "Int10_front_educ_faculty": {
        "Int9_front_poly_room": 53,
        "Int11_front_cbm": 76,
        "Int7_front_magsaysay": 70
    },
    "Int11_front_cbm": {
        "Int10_front_educ_faculty": 76,
        "CED Building": 9,
        "int6_front_sas": 73,
        "Int12_front_educ_elem": 46,
    },
    "CED Building": {
        "Int11_front_cbm": 9
    },
    "Int12_front_educ_elem": {
        "Int11_front_cbm": 46,
        "Int13_basketball_court": 15,
        "Int15_front_cbm_building": 75
    },
    "Int13_basketball_court": {
        "Int12_front_educ_elem": 15,
        "Int14_inside_building_right": 55
    },
    "Int15_front_cbm_building": {
        "Int12_front_educ_elem": 75,
        "Int1_guardpost": 38,
        "CBM Building": 7
    },
    "CBM Building": {
        "Int15_front_cbm_building": 7
    }

}


class LoginScreen(Screen):
    mobile_num = ObjectProperty(None)
    password = ObjectProperty(None)

    dialog = None

    def login_inter(self):
        if self.mobile_num.text == "123" and self.password.text == "123":
            self.show_input_dialog()
        else:
            Snackbar(text="Invalid credentials").open()

    def show_input_dialog(self):
        if not self.dialog:
            self.input_field = MDTextField(
                hint_text="Enter your name",
                size_hint_x=1
            )

            self.dialog = MDDialog(
                title="Welcome!",
                type="custom",
                content_cls=self.input_field,
                buttons=[
                    MDRaisedButton(
                        text="OK",
                        on_release=self.close_dialog
                    )
                ],
            )
        self.dialog.open()

    def close_dialog(self, obj):
        user_input = self.input_field.text
        Snackbar(text=f"Hello, {user_input}!").open()

        self.dialog.dismiss()
        self.manager.current = "homepage"


class SignupScreen(Screen):
    create_num = ObjectProperty(None)
    c_pass = ObjectProperty(None)
    v_pass = ObjectProperty(None)

    def signup_inter(self):
        if not self.create_num.text or not self.c_pass.text:
            self.manager.show_message("Please enter given fields.")
            return
        if self.create_num.text.isdigit():
            if int(self.create_num.text) in self.manager.students:
                self.manager.show_message("Account already exists with this number.")
                self.create_num.text = ""
                self.c_pass.text = ""
                self.v_pass.text = ""
                return
            if self.c_pass.text == self.v_pass.text:
                self.manager.students[int(self.create_num.text)] = self.c_pass.text
                self.manager.show_message("Successfully created an account")
                self.c_pass.text = ""
                self.v_pass.text = ""
                self.create_num.text = ""
            else:
                self.manager.show_message("verify password not similar to new password")
                self.v_pass.text = ""
        else:
            self.manager.show_message("Mobile number must be digits only.")
            return

    def go_back(self):
        self.manager.current = "login"


class HomeScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class PersonalInfoScreen(Screen):
    pass


class ScheduleScreen(Screen):
    subject = ObjectProperty(None)
    room = ObjectProperty(None)
    day = ObjectProperty(None)
    time_start = ObjectProperty(None)
    time_end = ObjectProperty(None)
    table_box = ObjectProperty(None)

    def on_pre_enter(self):

        if not hasattr(self, "table_created"):
            self.table_created = True
            self.create_table()

    def create_table(self):
        self.table = MDDataTable(
            use_pagination=True,
            column_data=[
                ("Subject", dp(18)),
                ("Room", dp(18)),
                ("Day", dp(18)),
                ("Time start", dp(18)),
                ("Time end", dp(18)),
            ],
            row_data=[],
            size_hint=(0.95, 0.35),
            pos_hint={"center_x": 0.5},
        )
        self.table_box.add_widget(self.table)

    def show_date(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.set_day)
        date_dialog.open()

    def set_day(self, instance, value, date_range):
        if isinstance(value, datetime.date):
            self.day.text = value.strftime("%A")

    def show_start_time(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.set_time)
        time_dialog.open()

    def set_time(self, instance, time_obj):
        self.time_start.text = time_obj.strftime("%I:%M %p")

    def show_end_time(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.end_set_time)
        time_dialog.open()

    def end_set_time(self, instance, time_obj):
        self.time_end.text = time_obj.strftime("%I:%M %p")

    def add_schedule(self):
        subject = self.subject.text.strip()
        room = self.room.text.strip().upper()
        day = self.day.text.strip()
        time_start = self.time_start.text.strip()
        time_end = self.time_end.text.strip()

        if all([subject, room, day, time_start, time_end]):
            self.table.row_data.append((subject, room, day, time_start, time_end))
            self.table.row_data = self.table.row_data.copy()

            self.subject.text = ""
            self.room.text = ""
            self.day.text = ""
            self.time_start.text = ""
            self.time_end.text = ""

    def day_picker(self):
        menu_items = [
            {
                "text": day,
                "viewclass": "OneLineListItem",
                "height": dp(48),
                "on_release": lambda x=day: self.set_day_value(x)
            }
            for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        ]

        self.day_menu = MDDropdownMenu(
            caller=self.ids.day,
            items=menu_items,
            width_mult=4
        )
        self.day_menu.open()

    def set_day_value(self, value):
        self.ids.day.text = value
        if hasattr(self, "day_menu"):
            self.day_menu.dismiss()

    def building_picker(self):
        menu_items = [
            {
                "text": building,
                "viewclass": "OneLineListItem",
                "height": dp(48),
                "on_release": lambda x=building: self.set_building_value(x)
            }
            for building in VALID_ROOMS.keys()
        ]

        self.building_menu = MDDropdownMenu(
            caller=self.ids.building,
            items=menu_items,
            width_mult=4
        )
        self.building_menu.open()

    def room_picker(self):
        if hasattr(self, "room_menu"):
            self.room_menu.open()

    def set_building_value(self, value):
        self.ids.building.text = value
        if self.building_menu:
            self.building_menu.dismiss()

        self.prepare_rooms_menu(value)

    def set_room_value(self, value):
        self.ids.room.text = value
        if self.room_menu:
            self.room_menu.dismiss()

    def prepare_rooms_menu(self, building_name):
        rooms_list = []
        building_data = VALID_ROOMS.get(building_name, {})
        if building_data:
            for floor_rooms in building_data["rooms"].values():
                rooms_list.extend(floor_rooms)

        menu_items = [
            {
                "text": room,
                "viewclass": "OneLineListItem",
                "height": dp(48),
                "on_release": lambda x=room: self.set_room_value(x)
            }
            for room in rooms_list
        ]

        self.room_menu = MDDropdownMenu(
            caller=self.ids.room,
            items=menu_items,
            width_mult=4
        )



class BuildingMarker(MapMarker):
    building_name = ""


def dijkstra(graph, start, end):
    dist = {node: float("inf") for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    unvisited = set(graph.keys())

    while unvisited:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)
        if dist[current] == float("inf"):
            break
        for neighbor, cost in graph[current].items():
            alt = dist[current] + cost
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current

    path = []
    node = end
    while node:
        path.insert(0, node)
        node = prev[node]
    return path

class RouteLine(MapLayer):
    def __init__(self, points, **kwargs):
        super().__init__(**kwargs)
        self.points = points

    def reposition(self):
        self.canvas.clear()
        mapview = self.parent
        if not mapview:
            return
        with self.canvas:
            Color(1, 0, 0, 1)
            pts = []
            for node in self.points:
                lat, lon = NODES[node]
                x, y = mapview.get_window_xy_from(lat, lon, mapview.zoom)
                pts.extend([x, y])
            if len(pts) >= 4:
                Line(points=pts, width=dp(3))


class MapScreen(Screen):
    mapview = ObjectProperty(None)
    menu = ObjectProperty(None)
    markers = []

    def dijkstra(self):
        pass

    def on_pre_enter(self):
        if not hasattr(self, "menu_created"):
            self.menu_created = True
            self.create_menu()
        self.mapview = self.ids.mapview
        self.markers = []

    def create_menu(self):
        menu_items = [
            {
                "text": day,
                "viewclass": "OneLineListItem",
                "height": dp(40),
                "on_release": lambda x=day: self.menu_callback(x),
            }
            for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        ]

        self.menu = MDDropdownMenu(
            caller=self.ids.toolbar,
            items=menu_items,
            width_mult=4,
        )

    def open_menu(self):
        if self.menu:
            self.menu.open()

    def menu_callback(self, day):
        self.menu.dismiss()
        self.show_markers_for_day(day)
        Snackbar(text=f"Showing schedule for {day}", duration=1.5).open()

    def show_building_dialog(self, building_name):
        building = VALID_ROOMS[building_name]

        room_text = "[b]Available Rooms[/b]\n\n"
        for floor, rooms in building["rooms"].items():
            room_text += f"[b]{floor}[/b]\n"
            for r in rooms:
                room_text += f" • {r}\n"
            room_text += "\n"

        schedule_screen = self.manager.get_screen("schedule")

        user_schedule = "[b]Your Schedule Here[/b]\n\n"
        has_schedule = False

        for entry in schedule_screen.table.row_data:
            subject, room, day, start, end = entry

            for _, rooms in building["rooms"].items():
                if room in rooms:
                    user_schedule += f"[b]{subject}[/b]\n"
                    user_schedule += f"Room: {room}\n"
                    user_schedule += f"Day: {day}\n"
                    user_schedule += f"Time: {start} - {end}\n\n"
                    has_schedule = True

        if not has_schedule:
            user_schedule += "No schedule found in this building.\n"

        dialog = MDDialog(
            title=building_name,
            text=room_text + "\n" + user_schedule,
            radius=[18, 18, 18, 18]
        )
        dialog.open()

    def show_markers_for_day(self, day):

        for marker in self.markers[:]:
            if marker.parent:
                self.mapview.remove_widget(marker)
        self.markers.clear()

        schedule_screen = self.manager.get_screen("schedule")

        if not hasattr(schedule_screen, "table") or schedule_screen.table is None:
            self.manager.show_message("No schedule table found — skipping marker creation.")
            return

        for entry in schedule_screen.table.row_data:
            subject, room, sched_day, time_start, time_end = entry

            if sched_day != day:
                self.manager.show_message(f"No available Subject in {day}")
                continue

            building_coords = None
            for building, data in VALID_ROOMS.items():
                for floor, rooms in data["rooms"].items():
                    if room in rooms:
                        building_coords = data["coords"]
                        break
                if building_coords:
                    break

            if not building_coords:
                self.manager.show_toast(f"Room {room} not in VALID_ROOMS")
                continue

            lat, lon = building_coords
            marker = BuildingMarker(lat=lat, lon=lon)
            marker.building_name = building
            marker.on_release = lambda m=marker: self.show_building_dialog(m.building_name)

            self.mapview.add_widget(marker)
            self.markers.append(marker)

    def show_markers(self):

        for name, (lat, lon) in Main_buildings.items():
            marker1 = MapMarker(lat=lat, lon=lon, source="marker.png")
            marker1.size = (dp(32), dp(32))  # set width and height
            marker1.size_hint = (None, None)
            self.mapview.add_widget(marker1)

        for name, (lat, lon) in INTERSECTIONS.items():
            marker = MapMarker(lat=lat, lon=lon, source="marker_blue.png")
            marker.size = (dp(32), dp(32))  # set width and height
            marker.size_hint = (None, None)  # disable automatic scaling
            self.mapview.add_widget(marker)

class InboxScreen(Screen):
    pass


class MainWindow(ScreenManager):
    students = {}

    def show_message(self, ms):
        Snackbar(text=ms, duration=1.5).open()

    def show_toast(self, ms):
        toast(text=ms, duration=1.5)


class KurikongApp(MDApp):
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_string(KV)

    def build_route(self, start, end):
        # Remove old routes
        for layer in list(self.mapview.children):
            if isinstance(layer, RouteLine):
                self.mapview.remove_widget(layer)

        path = dijkstra(GRAPH, start, end)
        print("PATH:", path)
        route = RouteLine(path)
        self.mapview.add_widget(route)

    def on_home(self):
        self.root.current = "homepage"

    def on_profile(self):
        self.root.current = "profile"

    def on_information(self):
        self.root.current = "information"

    def on_schedule(self):
        self.root.current = "schedule"

    def on_map(self):
        self.root.current = "map"

    def on_inbox(self):
        self.root.current = "inbox"


if __name__ == "__main__":
    KurikongApp().run()
