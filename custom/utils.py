import os
import hashlib


# function ida ne'ebe mak define hashed hodi encrypte kodigu dadus nian.
def getlastid(table_name):
	result = table_name.objects.last()
	if result:
		lastid = result.id
		newid = lastid + 1
	else:
		lastid = 0
		newid = 1
	return lastid, newid

def hash_md5(strhash):
	hashed = hashlib.md5(strhash.encode())
	return hashed.hexdigest()

# Function fulan nian
def getFulanID(fulan):
	if fulan == "January":
		fulanTetun = "Janeiru"
		fulanID = "1"
	if fulan == "February":
		fulanTetun = "Fevreiru"
		fulanID = "2"
	if fulan == "March":
		fulanTetun = "Marsu"
		fulanID = "3"
	if fulan == "April":
		fulanTetun = "Abril"
		fulanID = "4"
	if fulan == "May":
		fulanTetun = "Maiu"
		fulanID = "5"
	if fulan == "June":
		fulanTetun = "Junhu"
		fulanID = "6"
	if fulan == "Jully":
		fulanTetun = "Julhu"
		fulanID = "7"
	if fulan == "August":
		fulanTetun = "Agustu"
		fulanID = "8"
	if fulan == "September":
		fulanTetun = "Setembru"
		fulanID = "9"
	if fulan == "October":
		fulanTetun = "Outubru"
		fulanID = "10"
	if fulan == "November":
		fulanTetun = "Novembru"
		fulanID = "11"
	if fulan == "December":
		fulanTetun = "Dezembru"
		fulanID = "12"
	return fulanID, fulanTetun
	