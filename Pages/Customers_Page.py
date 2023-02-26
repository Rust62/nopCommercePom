from selenium.webdriver.common.by import By
from Config.Test_Data import TestData
from Pages.Base_Page import BasePage
from Pages.Home_Page import HomePage


class AddCustomer (BasePage):
    def __init__(self , driver):
        super ().__init__ ( driver )

    Customers_menu = (By.XPATH , "//a[@href='#']//p[contains(text(),'Customers')]")
    Customers_menu_item = (By.XPATH , "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")

    Add_new = (By.XPATH , "//a[@class='btn btn-primary']")
    Email = (By.XPATH , "//input[@id='Email']")
    Password = (By.XPATH , "//input[@id='Password']")
    First_name = (By.XPATH , "//input[@id='FirstName']")
    Last_name = (By.XPATH , "//input[@id='LastName']")
    Male_gender = (By.XPATH , "//input[@id='Gender_Male']")
    Female_gender = (By.XPATH , "//input[@id='Gender_Female']")
    Date_of_birth = (By.XPATH , "//input[@id='DateOfBirth']")
    Company_name = (By.XPATH , "//input[@id='Company']")
    Tax_exempt = (By.XPATH , "//input[@id='IsTaxExempt']")
    Newsletter = (By.XPATH , "//div[@class='input-group-append']//div[@role='listbox']")

    Customer_roles = (By.XPATH , "//div[@role='listbox']")
    Customer_roles_administrators = (By.XPATH , "//li[contains(text(), 'Administrators')]")
    btn_delete_administrator = (By.XPATH , "//span[@title='delete']")
    Customer_roles_forum_moderators = (By.XPATH , "//li[contains(text(), 'Forum Moderators')]")
    btn_delete_forum_moderators = (By.XPATH , "(//span[@title='delete'])[2]")
    Customer_roles_guests = (By.XPATH , "//li[contains(text(), 'Guests')]")
    btn_delete_guests = (By.XPATH , "(//span[@title='delete'])[3]")
    Customer_roles_registered = (By.XPATH , "//li[contains(text(), 'Registered')]")
    btn_delete_registered = (By.XPATH , "(//span[@title='delete'])[4]")
    Customer_roles_vendors = (By.XPATH , "//li[contains(text(), 'Vendors')]")
    btn_delete_vendors = (By.XPATH , "(//span[@title='delete'])[5]")
    customer_roles = (By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]")  # don't know what!!!
    btn_clear_Customer_roles = "//span[@title='clear']"

    Manager_of_vendor = (By.XPATH , "//select[@id='VendorId']")
    Admin_comment = (By.XPATH, "//textarea[@id='AdminComment']")
    Active_btn = (By.XPATH , "//input[@id='Active']")
    Admin_content = (By.XPATH , "//textarea[@id='AdminComment']")
    Save_btn = (By.XPATH , "//button[@name='save']")

    Add_success_alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissable']")


