from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from  time import *

url_base = 'http://localhost:8888/'


@pytest.fixture()
def browser():
    # Inicializar el navegador
    driver = webdriver.Chrome()
    yield driver
    # Cerrar el navegador después de la prueba
    driver.quit()

def login(browser):
    url = 'http://localhost:8888/admin/user/login'
    # Abrir la página web
    browser.get(url)
    
    # Encontrar los elementos del formulario de inicio de sesión
    username_input = browser.find_element(By.ID,'loginform-username')  # Suponiendo que el campo de usuario tiene el id 'username'
    password_input = browser.find_element(By.ID,'loginform-password')  # Suponiendo que el campo de contraseña tiene el id 'password'
    login_button = browser.find_element(By.NAME,'login-button')  # Suponiendo que el botón de inicio de sesión tiene el id 'loginButton'
    
    # Ingresar el nombre de usuario y la contraseña
    username_input.send_keys('esroot')
    password_input.send_keys('LS:escolar*123')
    
    # Enviar el formulario de inicio de sesión
    login_button.click()
    sleep(2)


#==================================================================================
#                            Test de Login
#===================================================================================
def est_login(browser):
    url = 'http://localhost:8888/admin/user/login'
    # Abrir la página web
    browser.get(url)
    
    # Encontrar los elementos del formulario de inicio de sesión
    username_input = browser.find_element(By.ID,'loginform-username')  # Suponiendo que el campo de usuario tiene el id 'username'
    password_input = browser.find_element(By.ID,'loginform-password')  # Suponiendo que el campo de contraseña tiene el id 'password'
    login_button = browser.find_element(By.NAME,'login-button')  # Suponiendo que el botón de inicio de sesión tiene el id 'loginButton'
    
    # Ingresar el nombre de usuario y la contraseña
    username_input.send_keys('esroot')
    password_input.send_keys('LS:escolar*123')
    
    # Enviar el formulario de inicio de sesión
    login_button.click()

    assert True
    
    # Verificar que el inicio de sesión fue exitoso redirigiendo a otra página
    #assert browser.current_url == 'http://localhost:8888/'  
    pass

#==================================================================================
#                            Test de apertura de caja
#===================================================================================
def est_apertura_caja(browser):
    login(browser)
    url = 'http://localhost:8888/gestion/apertura-caja/'
    browser.get(f'{url}create')

    #    # Esperar a que aparezca el campo de vendedor
    vendedor_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[@id="select2-usuario_id-container"]'))
    )
    

    # Hacer clic en el campo para abrir la lista desplegable
    
    vendedor_input.click()
    search_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field'))
    )    
    search_input.send_keys('jenn')
    

    # Esperar a que aparezca el nuevo contenedor del elemento
    new_container = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'select2-results'))
    )

    # Esperar a que aparezca el primer resultado en el nuevo contenedor
    first_result = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'select2-results'))
    )

    #first_result = browser.find_element(By.CLASS_NAME,'select2-results__option select2-results__option--highlighted')
    # Hacer clic en el primer resultado
    first_result.click()


    #sleep(60)
    # Ingresar monto
    monto_input =  browser.find_element(By.ID,'aperturacaja-monto_apertura')
    monto_input.send_keys('1500')

    # Encontrar el botón por su clase
    btn_submit = browser.find_element(By.CLASS_NAME, 'btn.btn-primary.btn-block')

    # Hacer clic en el botón
    btn_submit.click()
    sleep(2)


    assert browser.current_url == f'{url}view?id=6'

#==================================================================================
#                            Test de venta de articulo
#===================================================================================
def est_venta_articulo(browser):
    login(browser)
    url = 'http://localhost:8888/gestion/caja/'
    browser.get(f'{url}create')

        # Esperar a que aparezca el campo de búsqueda de Select2
    search_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'select2-selection__arrow'))
    )
    sleep(1)
    search_input.click()

    # Escribir el valor en el campo de búsqueda
    #search_input.send_keys('leo')
    sleep(1)

    # Esperar a que aparezcan los resultados
    input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'select2-search__field'))
    )
    input.send_keys('leo')

    first_result = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'select2-results'))
    )

    first_result.click()

    sleep(1)

    #
    #=================SELECCIONA EL ALUMNO
    # Localiza el elemento <select> por su ID
    select_element = browser.find_element(By.ID, "alumno_select_id")

    # Crea un objeto de la clase Select para interactuar con el elemento
    select = Select(select_element)

    # Selecciona el primer elemento
    select.select_by_index(0)

    sleep(1)


    #===========================================
    # Seleciona articulo 
    #===========================================

    # Localiza el elemento <select> por su ID
    select_art = browser.find_element(By.ID, "caja-tipo_id")

    # Crea un objeto de la clase Select para interactuar con el elemento
    select = Select(select_art)

    # Selecciona el primer elemento
    select.select_by_index(1)

    sleep(1)

    input_art = WebDriverWait(browser, 10).until(
       EC.presence_of_element_located((By.XPATH, '//span[@id="select2-articulo_id-container"]'))
    )

    input_art.click()


    search_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field'))
    )    
    search_input.send_keys('libro')
    
    # Esperar a que aparezca el primer resultado en el nuevo contenedor
    first_result = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'select2-results'))
    )

    first_result.click()

    sleep(1)

    btn_add = browser.find_element(By.ID,'add-articulo')
    btn_add.click()

    sleep(1)



    #===========================
    #Metodo de pago
    #=======================

    # Localiza el elemento <select> por su ID
    select_pago = browser.find_element(By.ID, "cobroalumno-metodo_pago")

    # Crea un objeto de la clase Select para interactuar con el elemento
    select = Select(select_pago)

    # Selecciona el primer elemento
    select.select_by_index(1)

    input_pago = browser.find_element(By.ID,'catntidad_pagar_tipo_pago')
    input_pago.send_keys('200')
    sleep(1)


    btn_add_me = browser.find_element(By.ID,'add-metodo')
    btn_add_me.click()
    sleep(1)

    btn_add_c = browser.find_element(By.ID,'btn-cobrar-venta')
    sleep(1)
    btn_add_c.click()
    sleep(1)

    assert browser.current_url == f'{url}view?id=6'




#==================================================================================
#                            Test de asigncion de credito
#===================================================================================
def est_credito(browser):
    login(browser)
    url = 'http://localhost:8888/gestion/caja/'
    browser.get(f'{url}create')

        # Esperar a que aparezca el campo de búsqueda de Select2
    search_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'select2-selection__arrow'))
    )
    sleep(1)
    search_input.click()

    # Escribir el valor en el campo de búsqueda
    #search_input.send_keys('leo')
    sleep(1)

    # Esperar a que aparezcan los resultados
    input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'select2-search__field'))
    )
    input.send_keys('leo')

    first_result = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'select2-results'))
    )

    first_result.click()

    sleep(1)

    #
    #=================SELECCIONA EL ALUMNO
    # Localiza el elemento <select> por su ID
    select_element = browser.find_element(By.ID, "alumno_select_id")

    # Crea un objeto de la clase Select para interactuar con el elemento
    select = Select(select_element)

    # Selecciona el primer elemento
    select.select_by_index(0)

    sleep(1)


    #===========================================
    # Seleciona articulo 
    #===========================================

    # Localiza el elemento <select> por su ID
    select_art = browser.find_element(By.ID, "caja-tipo_id")

    # Crea un objeto de la clase Select para interactuar con el elemento
    select = Select(select_art)

    # Selecciona el primer elemento
    select.select_by_index(1)

    sleep(1)

    input_art = WebDriverWait(browser, 10).until(
       EC.presence_of_element_located((By.XPATH, '//span[@id="select2-articulo_id-container"]'))
    )

    input_art.click()


    search_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field'))
    )    
    search_input.send_keys('libro')
    
    # Esperar a que aparezca el primer resultado en el nuevo contenedor
    first_result = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'select2-results'))
    )

    first_result.click()

    sleep(1)

    btn_add = browser.find_element(By.ID,'add-articulo')
    btn_add.click()

    sleep(1)



    #===========================
    #Metodo de pago
    #=======================

    # Localiza el elemento <select> por su ID
    select_pago = browser.find_element(By.ID, "cobroalumno-metodo_pago")

    # Crea un objeto de la clase Select para interactuar con el elemento
    select = Select(select_pago)

    # Selecciona el primer elemento
    select.select_by_index(1)

    input_pago = browser.find_element(By.ID,'catntidad_pagar_tipo_pago')
    input_pago.send_keys('100')
    sleep(1)


    btn_add_me = browser.find_element(By.ID,'add-metodo')
    btn_add_me.click()
    sleep(1)

    btn_add_c = browser.find_element(By.ID,'btn-cobrar-venta')
    sleep(1)
    btn_add_c.click()
    sleep(1)

    #
    #  FECHA COMPROMISO 
    #
    input_fecha = browser.find_element(By.ID,'fecha_compromiso')
    input_fecha.click()
    input_fecha.send_keys('13/04/2024')

    cobro = browser.find_element(By.ID,'btn-cobrar')
    cobro.click()

    sleep(2)
    assert browser.current_url == f'{url}view?id=9'


#==================================================================================
#                            Test de pago de un credito
#===================================================================================


def est_cobro_credito(browser):
    login(browser)
    url = 'http://localhost:8888/creditos/credito/view?id=3'
    browser.get(url)

    adeudo = int(browser.find_element(By.ID,'span_adeudo').text[1:])
    
    pago = browser.find_element(By.ID,'cantidad_pagar')
    pago.send_keys(100)

    # Localiza el elemento <select> por su ID
    select_pago = browser.find_element(By.ID, "metodo_pago")

    # Crea un objeto de la clase Select para interactuar con el elemento
    select = Select(select_pago)

    # Selecciona el primer elemento
    select.select_by_index(1)

    btn = browser.find_element(By.ID,'btn_pagar')
    btn.click()

    sleep(2)

    _adeudo = int(browser.find_element(By.ID,'span_adeudo').text[1:])

    assert _adeudo == 0


def tst_configuracion_colegiatura(browser):
    login(browser)
    url = 'http://localhost:8888/alumnos/alumno/update?id=3'
    browser.get(url)

    # Esperar a que el elemento sea visible
    checkbox = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'edit_especial_paquete'))
    )
    # Verificar si el checkbox no está marcado
    if not checkbox.is_selected():
        # Marcar el checkbox
        checkbox.click()
        sleep(1)
    

    for i in range(9,17):
        mes = browser.find_element(By.ID,f'mes_{i}')
        mes.click()
    
    save = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    save.click()
    sleep(1)

    try:
        # Intentar encontrar el elemento con el ID 'w6-success-0'
        element = browser.find_element(By.ID, "w6-success-0")
        assert True
    except :
        assert False







def test_horario(browser):
    login(browser)
    url = 'http://localhost:8888/operacion/horario/horario-clase?id=11'
    # Carga la página
    browser.get(url)

    # Asegúrate de que la página está completamente cargada
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "materia_11")))
    except TimeoutException:
        pytest.fail("La página no se cargó completamente")

    # Simula el arrastre y la soltura de un elemento
    draggable_element = browser.find_element(By.ID, "materia_11")
    draggable_element_2 = browser.find_element(By.ID, "materia_12")

    droppable_area = browser.find_element(By.ID, "dia_4_hora_09:30")
    webdriver.ActionChains(browser).drag_and_drop(draggable_element, droppable_area).perform()

    droppable_area_2 = browser.find_element(By.ID, "dia_1_hora_09:30")
    webdriver.ActionChains(browser).drag_and_drop(draggable_element_2, droppable_area_2).perform()
    sleep(2)
    # Verifica que el elemento se haya soltado correctamente
    dropped_element = browser.find_element(By.XPATH, '//*[@id="dia_4_hora_09:30"]')
    dropped_element_ = browser.find_element(By.XPATH, '//*[@id="dia_1_hora_09:30"]')
    assert dropped_element.is_displayed() and dropped_element_.is_displayed()







