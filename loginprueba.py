# Importamos el módulo unittest y la biblioteca Selenium
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Definimos la clase de prueba, que hereda de TestCase
class CalificacionDeAnime(unittest.TestCase):

    # Este método se ejecuta antes de cada prueba
    def setUp(self):
        # Creamos una instancia del controlador de Selenium para el navegador Edge
        self.driver = webdriver.Edge()

    # Esta es la prueba propiamente dicha
    def test_calificar_anime(self):
        # Simulamos el inicio de sesión en el sitio web
        self.driver.get("http://10.0.0.5/login.php")
        time.sleep(2)
        username = self.driver.find_element(By.ID,"Email")
        password = self.driver.find_element(By.ID,"Password")
        username.send_keys("bellacoz1911@gmail.com")
        password.send_keys("123")
        # Tomamos una captura de pantalla
        self.driver.get_screenshot_as_file("img/"+self.driver.name+".png")
        login_button = self.driver.find_element(By.ID,"btn-login")
        login_button.click()
        time.sleep(2)
        
        # agragamos un nuevo elemento
        self.driver.get("http://10.0.0.5/administrar_peliculas.php")
        time.sleep(2)
        nombre = self.driver.find_element(By.ID,"NameV")
        link = self.driver.find_element(By.ID,"LinkV")
        img = self.driver.find_element(By.ID, "IMG")
        
        nombre.send_keys("video generico")
        link.send_keys("ZRtdQ81jPUQ")
        img.send_keys("https://i.ytimg.com/an_webp/ZRtdQ81jPUQ/mqdefault_6s.webp?du=3000&sqp=CMCI_KEG&rs=AOn4CLC5KaBCZqtTSwYtD3OKHp6VzdGwnw")
        # Tomamos una captura de pantalla
        self.driver.get_screenshot_as_file("img/"+self.driver.name+".png")
        login_button = self.driver.find_element(By.ID,"saveMV")
        login_button.click()
        time.sleep(2)
        
        #revisamos que se agrego
        self.driver.get("http://10.0.0.5/")
        time.sleep(2)
        
        #volvemos a la pantalla anterior
        self.driver.get("http://10.0.0.5/administrar_peliculas.php")
        
        #editamos una pelicula
        
        Pbtnedit = self.driver.find_element(By.CSS_SELECTOR,"tr:nth-child(1) .btn-warning")
        Pbtnedit.click()
        time.sleep(2)
        
        nombre = self.driver.find_element(By.ID,"tit")
        nombre.send_keys("probando cambio de nombre")
        
        btnedit2 = self.driver.find_element(By.ID,"Btn-update")
        btnedit2.click()
        
        self.driver.get("http://10.0.0.5/")
        time.sleep(2)
        
        #volvemos a la pantalla anterior
        self.driver.get("http://10.0.0.5/administrar_peliculas.php")
        
        Pbtnedit = self.driver.find_element(By.CSS_SELECTOR,"tr:nth-child(1) .btn-danger")
        Pbtnedit.click()
        time.sleep(2)
        
        self.driver.get("http://10.0.0.5/")
        time.sleep(10)
        

    # Este método se ejecuta después de cada prueba
    def tearDown(self):
        # Cerramos el navegador
        self.driver.quit()

# Verificamos si este archivo es el programa principal
if __name__ == '__main__':
    # Ejecutamos todas las pruebas definidas en la clase CalificacionDeAnime
    unittest.main()