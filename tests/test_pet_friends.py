import os

from api import PetFriends
from settings import valid_email, valid_password
from settings import invalid_email, invalid_password
pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    status, result = pf.get_api_key(invalid_email, invalid_password)
    assert status == 403

def test_get_api_key_for_invalid_email(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(invalid_email, valid_password)
    assert status == 403

def test_get_api_key_for_invalid_password(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(valid_email, invalid_password)
    assert status == 403

def test_post_create_pet_with_novalid_key(name="Пес", animal_type="Собака", age=3):
    auth_key = {"key": '3dsf9sd8f9dsa8gadfh8dfh78dfh7daf7h8dfh78dfh78sdf7h8sdf7h'}

    status, result = pf.post_create_pet(auth_key,name,animal_type,age)
    assert status == 403

def test_post_new_pet_with_valid_data_novalid_key(name='Alesha', animal_type='sobaken',age='2', pet_photo='image\jpeg\dog.jpg'):
    auth_key = {"key": '3dsf9sd8f9dsa8gadfh8dfh78dfh7daf7h8dfh78dfh78sdf7h8sdf7h'}
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pf.post_add_pet(auth_key,name,animal_type,age,pet_photo)
    assert status == 400

def test_post_new_pet_with_null_data(name='', animal_type='',age='', pet_photo='image\jpeg\dog.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pf.post_add_pet(auth_key, name, animal_type, age,pet_photo)
    assert status == 400

def test_post_new_pet_with_null_data(name='', animal_type='',age='', pet_photo='image\jpeg\dog.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pf.post_add_pet(auth_key, name, animal_type, age,pet_photo)
    assert status == 400

def test_delete_pet_with_valid_data_novalid_key(pet_id=0):
    auth_key = {"key": '3dsf9sd8f9dsa8gadfh8dfh78dfh7daf7h8dfh78dfh78sdf7h8sdf7h'}
    status, _ = pf.delete_pet(auth_key,pet_id)
    assert status == 403

def test_put_pet_with_valid_data_novalid_key(pet_id='0',name='Шарик',animal_type='Собака', age=1):
    auth_key = {"key": '3dsf9sd8f9dsa8gadfh8dfh78dfh7daf7h8dfh78dfh78sdf7h8sdf7h'}
    status, result = pf.put_pet(auth_key,pet_id,name,animal_type,age)
    assert status == 403