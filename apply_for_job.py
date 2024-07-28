import asyncio
from playwright.async_api import async_playwright
import yaml
import re

class ApplyForJob:
    def __init__(self, filename_yaml:str, filename_pdf:str, url_job:str, credentials:str=None, session_token:str=None):
        self.filename = filename_yaml
        self.pdf = filename_pdf
        self.url_job = url_job
        self.domain = url_job.split('.com')[0] + '.com'
        self.path = url_job.split('.com')[1]
        self.session_token = session_token
        self.browser = None
        self.page = None
        self.credentials = credentials
        self.cv_data = None
    
    async def get_info(self) -> None:
        with open(self.filename, 'r', encoding='UTF-8') as f:
            self.cv_data = yaml.safe_load(f)              

    async def start(self):
        print("Starting application process...")
        async with async_playwright() as p:
            self.browser = await p.chromium.launch(**{'headless': True})
            # self.browser = await p.firefox.launch(**{'headless': True})
            context_options = {
                'user_agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1"
            }
            context = await self.browser.new_context(**context_options)
            
            self.page = await context.new_page()
            await self.page.goto(self.url_job, wait_until='networkidle')

            if self.session_token:
                await context.add_cookies([{
                    'name': '__Secure-next-auth.session-token',
                    'value': self.session_token,
                    'domain': self.domain,
                    'path': self.path,
                    'secure': True,
                    'httpOnly': True,
                    'sameSite': 'Lax'
                }])
                
            # await self.page.reload(wait_until='networkidle')
            # await self.page.reload(timeout=10000)
            # await self.page.reload()
            # await asyncio.sleep(5)

            await self.page.get_by_role('button', name='Solicitar').click()
            await asyncio.sleep(1.2)
            await self.page.get_by_role('button', name='Solicitar manualmente').click()
            
            await asyncio.sleep(10)      
            # await self.page.wait_for_load_state('networkidle')
            
            # Inicio de sesión
            await self.login()
            print("Logged in...")
            await asyncio.sleep(10)      
            
            # Obtención de la información
            await self.get_info()
            # await asyncio.sleep(1)      
            
            # Llenado de la información personal
            await self.my_information_page()
            print("My information page completed...")
            await asyncio.sleep(1)
            
            # Llenado de la información de experiencia
            await self.my_experience_page()
            print("My experience page completed...")
            await asyncio.sleep(1)
            
            # Llenado de las preguntas de aplicación
            await self.application_questions()
            print("Application questions completed...")
            await asyncio.sleep(1)
            
            # Llenado de registro voluntario de información
            await self.voluntary_disclosure()
            print("Voluntary disclosure completed...")
            await asyncio.sleep(1)            
            

    async def login(self)->None:
        with open(self.credentials, 'r') as f:
            credentials = yaml.safe_load(f).get('credentials')
                    
        await self.page.get_by_role('textbox',name="Dirección de correo electró").fill(credentials['email'])
        await asyncio.sleep(0.1)
        await self.page.get_by_role('textbox',name='Contraseña').fill(credentials['password'])
        await asyncio.sleep(0.1)
        await self.page.get_by_role('button', name='Conectar').click()
        await asyncio.sleep(2.5)
        # print('val = ',await self.page.query_selector('div[data-automation-id="errorMessage"]'))
        # try:
        #     alert = await self.page.locator('div[data-automation-id="errorMessage"]').text_content()
        #     if alert:
        #         print(f'Alert:\n{alert}')
        #         raise Exception("Login failed.")
        # except:
        #     pass
        
    async def my_information_page(self)->None:
        # ¿Cómo nos ha conocido?
        
        # await self.page.get_by_role('textbox').click()
        # how_met_us = self.page.locator('input[id="input-1"]')
        # how_met_us = self.page.locator('input[data-uxi-widget-type="selectinput"]')
        # # await how_met_us.wait_for()
        how_met_us = self.page.get_by_role("textbox",name='¿Cómo nos ha conocido?')
        await how_met_us.fill('LinkedIn')
        await asyncio.sleep(0.1)
        await how_met_us.press('Enter')
        await asyncio.sleep(0.1)
        # Si has trabajado en Rappi, responde las siguientes preguntas: #1 Si, #2 No
        await self.page.click('input[type="radio"][id="2"]')
        await asyncio.sleep(0.1)
        await self.page.dblclick('input[type="radio"][id="2"]')
        await asyncio.sleep(0.1)
        # Obtención de la información personal        
        personal_info = self.cv_data.get('informacion_personal')
        # Nombre
        await self.page.get_by_role('textbox', name='Nombre').fill(personal_info.get('nombre'))
        await asyncio.sleep(0.1)
        # Apellido paterno
        await self.page.get_by_role('textbox', name='Apellido paterno').fill(personal_info.get('apellido_paterno'))
        await asyncio.sleep(0.1)
        # Apellido materno
        await self.page.get_by_role('textbox', name='Apellido materno').fill(personal_info.get('apellido_materno'))
        await asyncio.sleep(0.1)
        # Dirección
        await self.page.get_by_role('textbox', name='Línea de dirección 1').fill('na')
        await asyncio.sleep(0.1)
        # Colonia        
        await self.page.get_by_role('textbox', name='Colonia').fill('na')
        await asyncio.sleep(0.1)
        # Código postal
        pattern_location = re.compile(r'\d{5}')
        location = personal_info.get('ubicacion')
        await self.page.get_by_role('textbox', name='Código postal').fill(pattern_location.search(location)[0])
        await asyncio.sleep(0.1)
        # Ciudad
        await self.page.get_by_role('textbox', name='Ciudad').fill(location.split(',')[0])
        await asyncio.sleep(0.1)
        # Tipo de teléfono
        await self.page.get_by_role('button', name='Mobile').click()
        await asyncio.sleep(0.1)
        # Número de teléfono
        phone = personal_info.get('numero_telefono')
        phone_numer = None
        if len(phone) >= 10:
            pattern_phone = re.compile(r'\+\d{1,2}')
            contry_code = pattern_phone.search(phone)[0]
            phone_numer = phone.split(contry_code)[1]
        else:
            phone_numer = "0000000000"
        await self.page.get_by_role('textbox', name='Número de teléfono').fill(phone_numer)
        await asyncio.sleep(0.1)
        await self.page.get_by_role('button', name='Guardar y continuar').click()
        
        
    async def my_experience_page(self)->None:
        # Título del puesto
        await self.page.get_by_role('textbox', name='Título de puesto').fill('puesto')
        await asyncio.sleep(0.1)
        # Empresa
        await self.page.get_by_role('textbox', name='Empresa').fill('empresa')
        await asyncio.sleep(0.1)
        # Ubicación
        await self.page.get_by_role('textbox', name='Ubicación').fill('ubicación')
        await asyncio.sleep(0.1)
        # Actualmente trabajando
        # await self.page.click('input[type="checkbox"][id="input-19"]')
        await asyncio.sleep(0.1)
        # Desde 
        await self.page.fill('input[role="spinbutton"][id="input-22-dateSectionMonth-input"]', value='01')
        await asyncio.sleep(0.1)
        await self.page.fill('input[role="spinbutton"][id="input-22-dateSectionYear-input"]', value='2020')
        await asyncio.sleep(0.1)
        # Hasta
        await self.page.fill('input[role="spinbutton"][id="input-25-dateSectionMonth-input"]', value='02')
        await asyncio.sleep(0.1)
        await self.page.fill('input[role="spinbutton"][id="input-25-dateSectionYear-input"]', value='2024')
        await asyncio.sleep(0.1)
        # Descripción del rol
        await self.page.fill('textarea[data-automation-id="description"]', value='descripción')
        await asyncio.sleep(0.1)
        # Más experiencias
        # await self.page.get_by_role('button', name='Añadir más').click() 
        # await asyncio.sleep(1)
        # Hablidades
        skills = ['skill1', 'skill2', 'skill3']
        for skill in skills:
            await self.page.get_by_placeholder('Buscar',exact=True).fill(value=skill)
            await self.page.get_by_placeholder('Buscar',exact=True).press('Enter')
            await asyncio.sleep(0.1)
        # Subir CV
        async with self.page.expect_file_chooser() as fc_info:
            await self.page.get_by_text("Seleccionar archivos").click()
        file_chooser = await fc_info.value
        await file_chooser.set_files(self.pdf) # ACTUALIZAR por el nombre del archivo (Validar su existencia)
        await asyncio.sleep(0.1)
        # Linkedin
        await self.page.get_by_role('textbox', name='Linkedin').fill('http://www.linkedin.com/in/perfil') # https://www.linkedin.com/in/...
        await asyncio.sleep(0.1)
        await self.page.get_by_role('button', name='Guardar y continuar').click()
                            
    async def application_questions(self) -> None:
        # ¿Por qué quieres unirte a la familia Rappi?
        await self.page.fill('textarea[data-automation-id="1dcc48d740561000fb2fd8194feb0000"]', value='Porque me gusta la empresa')
        # await self.page.fill('textarea[id="input-61"]', value='na')
        await asyncio.sleep(0.1)
        # Cuéntanos lo más extraordinario que has hecho a nivel profesional
        await self.page.fill('textarea[data-automation-id="1dcc48d740561000fb2fd8b39b4c0000"]', value='na')
        await asyncio.sleep(0.1)
        # En cuanto a tu experiencia. Cuál es tu relación con el rol?
        await self.page.fill('textarea[data-automation-id="1dcc48d740561000fb2fd8b39b4c0001"]', value='na')
        await asyncio.sleep(0.1)
        # ¿Cuál es tú salario actual o cual fue tú ultimo salario?
        await self.page.fill('textarea[data-automation-id="1dcc48d740561000fb2fd8b39b4c0002"]', value='na')
        await asyncio.sleep(0.1)
        # ¿Cuál es tu aspiración salarial?
        await self.page.fill('textarea[data-automation-id="1dcc48d740561000fb2fd8b39b4c0003"]', value='na')
        # await self.page.fill('textarea[id="input-69"]', value='na')
        await asyncio.sleep(0.1)
        # ¿Cuál es tu nivel de ingles?  
        english_lvl = self.page.get_by_label('¿Cuál es tu nivel de ingles?')
        await english_lvl.press('I')
        await asyncio.sleep(0.1)
        await english_lvl.press('Enter')
        await asyncio.sleep(0.1)
        # ¿Cual es tu nivel de Portugués?
        portugues_lvl = self.page.get_by_label('¿Cual es tu nivel de Portugués?')
        await portugues_lvl.press('I')
        await asyncio.sleep(0.1)
        await portugues_lvl.press('Enter')
        await asyncio.sleep(0.1)
        # ¿Tienes conocimiento en SQL?
        sql_knowledge = self.page.get_by_label('¿Tienes conocimiento en SQL?')
        await sql_knowledge.press('S')
        await asyncio.sleep(0.1)
        await sql_knowledge.press('Enter')
        await asyncio.sleep(0.1)
        # Cuéntanos los lenguajes / tecnologías que dominas o has trabajado.
        await self.page.fill('textarea[data-automation-id="1dcc48d740561000fb2fd94d88530002"]', value='na')        
        await asyncio.sleep(0.1)
        await self.page.get_by_role('button', name='Guardar y continuar').click()
        
    async def voluntary_disclosure(self) -> None:
        # Sexo
        sex = self.page.get_by_role('button', name='Sexo Seleccione un valor required')
        # sex = self.page.locator('input[type="button"][data-automation-id="gender"]')
        await sex.click()
        await asyncio.sleep(0.1)
        await sex.press('M')
        await asyncio.sleep(0.1)
        await sex.press('Enter')
        await asyncio.sleep(0.1)
        # Fecha de nacimiento (opcional)
        await self.page.fill('input[role="spinbutton"][data-automation-id="dateSectionDay-input"]', value='01')
        await asyncio.sleep(0.1)
        await self.page.fill('input[role="spinbutton"][data-automation-id="dateSectionMonth-input"]', value='01')
        await asyncio.sleep(0.1)
        await self.page.fill('input[role="spinbutton"][data-automation-id="dateSectionYear-input"]', value='1998')
        await asyncio.sleep(0.1)
        # Ciudad de Nacimiento (opcional)
        await self.page.fill('input[type="text"][data-automation-id="cityOfBirth"]', value='ciudad')
        await asyncio.sleep(0.1)
        # He leido las condiciones y las acepto
        await self.page.click('input[type="checkbox"][data-automation-id="agreementCheckbox"]')
        await asyncio.sleep(0.1)
        await self.page.get_by_role('button', name='Guardar y continuar').click()

    async def close(self):
        await self.page.close()
        await self.browser.close()

async def apply_job(filename_yaml:str, filename_pdf:str, route:str, credentials:str) -> None:
    session = ApplyForJob(filename_yaml, filename_pdf, route, credentials)
    try:
        await session.start()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await session.close()
        print("Application job finished.") 