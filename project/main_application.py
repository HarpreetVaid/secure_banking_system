from side_menu import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap, Qt
import requests
import os

class mainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Secure Banking System")
        self.login_status = False
        self.profile_pic_path_open = None
        self.signature_pic_path_open = None
        self.username = None
        self.password = None
        self.token = None
        self.anti_csrf_token = None
        self.url = r"127.0.0.1:8000"
        self.signature_pic_path_open_profile = r'C:\Users\acer\Desktop\project\signature.png'
        self.user_profile = r'C:\Users\acer\Desktop\project\user.png'
        self.accountt_info.clicked.connect(self.switch_to_account_info_page)
        self.add_money.clicked.connect(self.switch_to_deposit_page)
        self.balance.clicked.connect(self.switch_to_balance_page)
        self.withdraw_money.clicked.connect(self.switch_to_withdraw_page)
        self.delete_account.clicked.connect(self.switch_to_delete_account_page)
        self.open_account.clicked.connect(self.switch_to_open_account_page)
        self.login_button.clicked.connect(self.switch_to_login_page)
        self.login_button_page.clicked.connect(self.login_btn_clicked)
        self.search_account_info.clicked.connect(self.get_acccount_info)
        self.search_button_check_balance.clicked.connect(self.show_balance_func)
        self.delete_account_button_page.clicked.connect(self.delete_account_func)
        self.deposit_button_withdraw.clicked.connect(self.withdraw_money_func)
        self.open_button_open_account.clicked.connect(self.account_open_func)
        self.picture_button_open_account.clicked.connect(self.profile_pic_set_open)
        self.signature_upload_button_open_account.clicked.connect(self.signature_pic_set_open)

    def switch_to_account_info_page(self):       
        if self.login_status:
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.accountt_info.setChecked(False)

    def switch_to_account_info_page_details(self):
        if self.login_status:
            self.stackedWidget.setCurrentIndex(1)

    def switch_to_balance_page(self):
        if self.login_status:
            self.stackedWidget.setCurrentIndex(2)
        else:
            self.balance.setChecked(False)

    def switch_to_deposit_page(self):
        if self.login_status:
            self.stackedWidget.setCurrentIndex(3)
        else:
            self.add_money.setChecked(False)

    def switch_to_withdraw_page(self):
        if self.login_status:
            self.stackedWidget.setCurrentIndex(4)
        else:
            self.withdraw_money.setChecked(False)

    def switch_to_open_account_page(self):
        if self.login_status:
            self.stackedWidget.setCurrentIndex(5)
        else:
            self.open_account.setChecked(False)

    def switch_to_login_page(self):
        if self.login_status:
            self.stackedWidget.setCurrentIndex(6)

    def switch_to_delete_account_page(self):
        if self.login_status:
            self.stackedWidget.setCurrentIndex(7)
        else:
            self.delete_account.setChecked(False)


    def download_image(url, local_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_path, 'wb') as file:
                file.write(response.content)
            return local_path
        return None

    def login_btn_clicked(self):
        self.username = self.username_field.text()
        self.password = self.password_field.text()
        if self.username and self.password:
            credentials = {'username': self.username, 'password': self.password}
            url = f'http://{self.url}/api/v1/login/'  
            try:
                response = requests.post(url, json=credentials)
                if response.status_code == 200:
                    try:
                        self.token = response.json().get('token')
                        print(f'Token: {self.token}')
                        if self.token:
                            self.login_status = True
                        self.switch_to_account_info_page()
                    except ValueError:
                        self.login_failed_text.setStyleSheet("color: red")
                        self.login_failed_text.setText("OOPS Something Went Wrong")
                        self.login_failed_text.repaint()
                        self.login_failed_text.show()
                        print('Response is not in JSON format')
                else:
                    self.login_failed_text.setStyleSheet("color: red")
                    self.login_failed_text.setText("Invalid Username or Password")
                    
                    self.login_failed_text.show()
                    print(f'Login failed: Status code {response.status_code}, Response: {response.text}')
                   
            except requests.exceptions.RequestException as e:
                self.login_failed_text.setStyleSheet("color: red")
                self.login_failed_text.setText("OOPS Something Went Wrong")
                self.login_failed_text.repaint()
                self.login_failed_text.show()
                print(f'Error occurred during login request: {e}')


    # account info page first
    def get_acccount_info(self):
        account = self.username_field_acc.text()
        if (len(account.strip())==0) or not account.strip().isdigit():
            self.switch_to_account_info_page()
        else:
            self.show_account_info_detail(account)

    def scaled_pixmap(self, filename, widget):
        pixmap = QPixmap(filename)
        scaled_pixmap = pixmap.scaled(widget.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        return scaled_pixmap

    def download_image(self,url, local_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_path, 'wb') as file:
                file.write(response.content)
            return local_path
        return None

    # account info page detail
    def show_account_info_detail(self, account):
        login_url = f'http://{self.url}/api/v1/login/'  # Correct URL schema
        credentials = {'username': self.username, 'password': self.password}
        login_response = requests.post(login_url, json=credentials)
        account_info = None

        if login_response.status_code == 200 or login_response.status_code == 201:
            auth_token = login_response.json().get('token')
            print("Authentication successful. Token:", auth_token)
            account_id = int(account)
            balance_url = f'http://{self.url}/api/v1/accounts/{account_id}/'
            headers = {
                'Authorization': f'Token {auth_token}'
            }
            response = requests.get(balance_url, headers=headers)
            account_info = response.json()
            print(account_info)
            print(response.json())
        else:
            print("Authentication failed.")
            return

        self.name_account_info.setText(account_info['name'])
        self.account_no_value_accinfo.setText(str(account_info['account_no']))
        self.balance_value_account_info_value.setText(str(account_info['balance']))
        # Set account info in your UI elements

        profile_pic_url = account_info['profile_pic']
        if profile_pic_url:
            profile_pic_path = os.path.join(os.getcwd(), "profile_pics", "user.png")  # Correct path
            self.download_image(profile_pic_url, profile_pic_path)

            profile_pic = QPixmap(profile_pic_path)
            self.pic_account_info.setPixmap(profile_pic)

        signature_pic_url = account_info['signature']
        if signature_pic_url:
            signature_pic_path = os.path.join(os.getcwd(), "signatures", "signature.png")  # Correct path
            self.download_image(signature_pic_url, signature_pic_path)

            signature_pic = QPixmap(signature_pic_path)
            self.signature_account_info.setPixmap(signature_pic)

        self.switch_to_account_info_page_details()


    # show Balance 
    def show_balance_func(self):
        account = self.username_field_check_balance.text()
        login_url = f'http://{self.url}/api/v1/login/'
        credentials = {'username': self.username, 'password': self.password}
        login_response = requests.post(login_url, json=credentials)

        if login_response.status_code == 200:
            auth_token = login_response.json().get('token')
            print("Authentication successful. Token:", auth_token)
            account_id = account 
            balance_url = f'http://{self.url}/api/v1/accounts/{account_id}/balance/'
            headers = {
                'Authorization': f'Token {auth_token}'
            }

            balance_response = requests.get(balance_url, headers=headers)
            print(balance_response.status_code)
            print(balance_response.json())
            self.value_label_check_balance.setStyleSheet("color: black ;\n font : 10pt")
            self.value_label_check_balance.setText(f'Balance is {balance_response.json().get("balance")}')
        else:
            print("Authentication failed.")

    def delete_account_func(self):
        account = self.username_field_2.text()

        delete_url = f'http://{self.url}/api/v1/accounts/{account}/'
        login_url = f'http://{self.url}/api/v1/login/'
        credentials = {'username': self.username, 'password': self.password}
        login_response = requests.post(login_url, json=credentials)
        headers = {
        'Authorization': f"Token {login_response.json().get('token')}",
        }
        response = requests.delete(delete_url, headers=headers)

        if response.status_code == 204:
            self.login_failed_text_2.setText(f"Account {account} deleted successfully.")
        else:
            self.login_failed_text_2.setText(f"Failed to delete account {account}. Status code: {response.status_code}")


    # add money
    def add_money_func(self):
        account = self.username_field_deposit_value.text()
        amount = self.amount_field_deposit.text()
        login_url = f'http://{self.url}/api/v1/login/'
        credentials = {'username': self.username, 'password': self.password}
        login_response = requests.post(login_url, json=credentials)

        if login_response.status_code == 200:
            auth_token = login_response.json().get('token')
            print("Authentication successful. Token:", auth_token)
            account_id = account 
            balance_url = f'http://{self.url}/api/v1/accounts/{account_id}/balance/'
            headers = {
                'Authorization': f'Token {auth_token}',
                'Content-Type': 'application/json'
            }
            
            balance_response = requests.get(balance_url, headers=headers)
            print(balance_response.status_code)
            print(balance_response.json())
            balance = float(balance_response.json().get('balance'))+float(amount)
            data = {
                'balance': balance  
                }

            update_response = requests.patch(balance_url, headers=headers, json=data)
            print(update_response.status_code)
            print(update_response.json())

        else:
            print("Authentication failed.")

        self.status_label_add_money.setText(account+"  "+amount)

    # withdraw money
    def withdraw_money_func(self):
        account = self.username_field_withdraw_value.text()
        amount = self.amount_field_withdraw.text()

        self.status_label_withdraw.setText(account+"  "+amount)


    # upload a file path
    def upload_a_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(None,"Select a file")
        return file_path
    
    # upload a profile_pic
    def profile_pic_set_open(self):
        path = self.upload_a_file()
        self.profile_pic_path_open = path
        profile_pic = QPixmap(self.scaled_pixmap(path,self.picture_label_open_account)) 
        self.picture_label_open_account.setPixmap(profile_pic)

    # upload a signature_pic
    def signature_pic_set_open(self):
        path = self.upload_a_file()
        self.signature_pic_path_open = path
        profile_pic = QPixmap(self.scaled_pixmap(path,self.signature_label_open_account)) 
        self.signature_label_open_account.setPixmap(profile_pic)


    # open account
    def account_open_func(self):
        username = self.username_lineEdit_open_account.text()
        u_id = self.account_number_lineEdit_open_account.text()
        money = self.amount_lineEdit_open_account.text()
        login_url = f'http://{self.url}/api/v1/login/'
        credentials = {'username': 'Harry', 'password': 'Harry@123'}
        response = requests.post(login_url, json=credentials)

        auth_token = response.json().get('token')

        if response.status_code == 200 and auth_token:
            print("Authentication successful. Token:", auth_token)
        else:
            print("Authentication failed.")

        response_csrf = requests.get(f'http://{self.url}/api/v1/csrf-token/')

        csrf_token = response_csrf.json().get('csrfToken')

        headers = {
            'Authorization': f'Token {auth_token}',
            'X-CSRFToken': csrf_token
        }

        url = f'http://{self.url}/api/v1/accounts/'
        data = {
            'name': username,
            'unique_id': u_id,
            'balance': money,
        }

        if self.profile_pic_path_open and self.signature_pic_path_open :
            files = {
                'profile_pic': open(self.profile_pic_path_open, 'rb'),
                'signature': open(self.signature_pic_path_open, 'rb')
            }

        response = requests.post(url, headers=headers, data=data, files=files)
        print(response.status_code)
        print(response.json())
        if response.status_code == 201:
            self.status_label_open_account.setStyleSheet("color: green")
            self.status_label_open_account.setText(f"Sucess : {response.json().get('account_no')}")
            self.status_label_open_account.show()





