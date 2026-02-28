import pandas as pd
from app.database import SessionLocal
from app.models.registros import Registros
from app.models.crime import Crime
from app.models.location import Location
from app.models.user import User

csv_path = 'csvv/crimes_violentos_2025.csv'
df = pd.read_csv(csv_path, sep=';')

db = SessionLocal()

# Busca/cria Crime
def get_crime_id(nome):
	crime = db.query(Crime).filter_by(nome=nome).first()
	if not crime:
		crime = Crime(nome=nome)
		db.add(crime)
		db.commit()
		db.refresh(crime)
	return crime.id

# Busca/cria Location
def get_location_id(cod_municipio, risp, rmbh, nome_municipio):
	location = db.query(Location).filter_by(cod_municipio=cod_municipio).first()
	if not location:
		location = Location(
			cod_municipio=cod_municipio,
			risp=risp,
			rmbh=rmbh,
			nome_municipio=nome_municipio
		)
		db.add(location)
		db.commit()
		db.refresh(location)
	return location.id

# Busca/cria User (exemplo: usuário padrão)
def get_user_id():
	user = db.query(User).filter_by(email='default@import.com').first()
	if not user:
		user = User(name='Importador', email='default@import.com', senha='123', adm=False)
		db.add(user)
		db.commit()
		db.refresh(user)
	return user.id

for _, row in df.iterrows():
	crime_id = get_crime_id(row['natureza'])
	location_id = get_location_id(
		cod_municipio=row['cod_municipio'],
		risp=row['risp'],
		rmbh=row['rmbh'],
		nome_municipio=row['municipio']
	)
	user_id = get_user_id()

	registro = Registros(
		qtd=row['registros'],
		mes=row['mes'],
		ano=row['ano'],
		crime_id=crime_id,
		location_id=location_id,
		user_id=user_id
	)
	db.add(registro)

db.commit()
db.close()
