import unittest
import requests
import re

class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/"
    number = {"nm": "111102445566778899"}
    test2 =['bin: 111102', 'brand: PRIVATE LABEL', 'type: DEBIT', 'category: None', 'issuer: None',
     'alpha_2: US', 'alpha_3: USA', 'country: United States', 'latitude: 37.0902', 'longitude: -95.7129',
      'bank_phone: None', 'bank_url: None']

    unvalid_number1 = {"nm": "111"}
    unvalid_number2 = {"nm": "644532445566778899ff"}
    unvalid_number3 = {"nm": "644532445566778899"}
    URL2 = "http://127.0.0.1:5000/card/111102445566778899"
    URL3 = "http://127.0.0.1:5000/card/111"
    URL4 = "http://127.0.0.1:5000/644532445566778899ff"
    URL5 = "http://127.0.0.1:5000/card/644532445566778899"

    

    def test_1(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        print("Test 1 OK")

    def test_2(self):
        resp = requests.post(self.URL, data=self.number)
        self.assertEqual(resp.status_code,200)
        mystr = resp.text
        mylist = mystr.split("<tr>")[1:]
        for i in range(len(mylist)):
            inf = re.findall(r'\>(.*?)\<', mylist[i])[0]
            inf = inf[1:len(inf) - 1]
            mylist[i] = inf

        self.assertEqual(mylist, self.test2)
        print("Test 2 OK")

    def test_3(self):
        resp = requests.post(self.URL, data=self.unvalid_number1)
        self.assertEqual(resp.status_code,500)
        self.assertEqual(re.findall(r'\>(.*?)\<', resp.text)[2], "Incorrect number")
        print("Test 3 OK")

    def test_4(self):
        resp = requests.post(self.URL, data=self.unvalid_number2)
        self.assertEqual(resp.status_code,500)
        self.assertEqual(re.findall(r'\>(.*?)\<', resp.text)[2], "Incorrect number")
        print("Test 4 OK")
    
    def test_5(self):
        resp = requests.post(self.URL, data=self.unvalid_number3)
        self.assertEqual(resp.status_code,500)
        self.assertEqual(re.findall(r'\>(.*?)\<', resp.text)[2], "No such card in database")
        print("Test 5 OK")

    def test_6(self):
        resp = requests.get(self.URL2)
        self.assertEqual(resp.status_code,200)
        mystr = resp.text
        mylist = mystr.split("<tr>")[1:]
        for i in range(len(mylist)):
            inf = re.findall(r'\>(.*?)\<', mylist[i])[0]
            inf = inf[1:len(inf) - 1]
            mylist[i] = inf

        self.assertEqual(mylist, self.test2)
        print("Test 6 OK")



if __name__ == "__main__":
    tester = TestAPI()
    tester.test_1()
    tester.test_2()
    tester.test_3()
    tester.test_4()
    tester.test_5()
    tester.test_6()
