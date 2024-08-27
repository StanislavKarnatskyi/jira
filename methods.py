# sender Kyiv
# Sklyarenka 5

sender_from_address = {
    "CitySender": "8d5a980d-391c-11dd-90d9-001a92567626",
    "Sender": "fdc96d91-77e0-11e9-9937-005056881c6b",
    "SenderAddress": "590fa4bd-7e8a-11ec-8513-b88303659df5",
    "ContactSender": "eaeec46f-ea91-11ee-a60f-48df37b921db",
}


# sender Kyiv
# warehouse 66

sender_from_warehouse = {
    "CitySender": "8d5a980d-391c-11dd-90d9-001a92567626",
    "Sender": "fdc96d91-77e0-11e9-9937-005056881c6b",
    "SenderAddress": "7b422fa4-e1b8-11e3-8c4a-0050568002cf",
    "ContactSender": "eaeec46f-ea91-11ee-a60f-48df37b921db",
}


# sender Berehove
# warehouse 1

#  todo add


# recipient Berehove

berehove = {
    "CityRecipient": "db5c88ca-391c-11dd-90d9-001a92567626",  # getCitiesRef
    "Recipient": "bf864b10-7816-11ea-8513-b88303659df5",  # бралось з getCounterparties recipient.
    # брав саме компанію. скоріш за все, однакове для всіх в компанії
    "RecipientAddress": "5a39e572-e1c2-11e3-8c4a-0050568002cf",  # getWarehouseRef only warehouses for now
    "ContactRecipient": "214aa1df-b18a-11ec-92e7-48df37b921da",
    # брав з getCounterpartyContactPersons обирав саме RecipientRef і так отримав
    "RecipientsPhone": "380684153954", }

# recipient Lviv

lviv = {
    "CityRecipient": "db5c88f5-391c-11dd-90d9-001a92567626",  # getCitiesRef
    "Recipient": "bf864b10-7816-11ea-8513-b88303659df5",  # бралось з getCounterparties recipient.
    "RecipientAddress": "d8e576e5-2a53-11ef-bcd0-48df37b921da",  # getCounterpartyAddresses
    "ContactRecipient": "d8bd4741-2a53-11ef-bcd0-48df37b921da",  # брав з getCounterpartyContactPersons обирав саме RecipientRef і так отримав
    "RecipientsPhone": "380633492262",
    "NumberOfFloorsLifting": "4"
}

# recipient Vinnytsia

vinnytsia = {
    "CityRecipient": "db5c88de-391c-11dd-90d9-001a92567626",  # getCitiesRef
    "Recipient": "bf864b10-7816-11ea-8513-b88303659df5",  # бралось з getCounterparties recipient.
    "RecipientAddress": "cc55c640-8462-11ee-a60f-48df37b921db",  # getCounterpartyAddresses
    "ContactRecipient": "0e9a2738-8aa9-11ee-a60f-48df37b921db",
    # брав з getCounterpartyContactPersons обирав саме RecipientRef і так отримав
    "RecipientsPhone": "380688079625",
    "NumberOfFloorsLifting": "4"
}


# create user
"""
    create user from jira data. only ukrainian language allowable
     

    fields
        first_name
        second_name
        last_name
        phone
    
    info for receive 
        response['data'][0]['Ref']
        response['data'][0]['ContactPerson']['data'][0]['Ref']
    
    fields in request for creating parcel
        Recipient == response['data'][0]['Ref']
        ContactRecipient == response['data'][0]['ContactPerson']['data'][0]['Ref']
"""

create_user = {
        "apiKey": 'API_Key',
        "modelName": "CounterpartyGeneral",
        "calledMethod": "save",
        "methodProperties": {
            "FirstName": 'first_name',  # from Jira // mandatory
            # "MiddleName": middle_name,  # from Jira // not mandatory
            "LastName": 'second_name',  # from Jira // mandatory
            "Phone": 'phone',  # form Jira // mandatory
            "CounterpartyType": "PrivatePerson",  # to check // if field ЄДРПОУ not empty then need to change methodProperties // todo
            "CounterpartyProperty": "Recipient"  # default
        }
    }

# find city
"""
    find warehouse from jira data. 
    return biggest city. if in jira field more information, like region, return more precise 
    
    fields 
        city
        
    info for receive 
        response['data'][0]['Addresses'][0]['Ref']
"""

find_city = {
        "apiKey": 'API_Key',
        "modelName": "AddressGeneral",
        "calledMethod": "searchSettlements",
        "methodProperties": {
            "CityName": 'city',
        }
}

# find warehouse
"""
    find warehouse from jira data. 
    return biggest city. if in jira field more information, like region, return more precise 
    
    fields 
        city
        warehouse_id
        
    info for receive 
        response['data'][0]['Ref']
"""

find_warehouse = {
        "apiKey": 'API_Key',
        "modelName": "AddressGeneral",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "FindByString": "",
            "CityName": 'city',
            "Page": "1",
            "Limit": "50",
            "Language": "UA",
            "WarehouseId": 'warehouse_id'
        }
}


# create parcel

var = {
        "apiKey": 'API_Key',
        "modelName": "InternetDocumentGeneral",
        "calledMethod": "save",
        "methodProperties": {
            "PayerType": "Sender",
            "PaymentMethod": "NonCash",
            "DateTime": 'today',
            "CargoType": "Parcel",
            "Weight": "0.5",  # dynamic parameter // need to manually enter
            "ServiceType": "WarehouseWarehouse",  # dynamic parameter
            "SeatsAmount": "1",  # dynamic parameter // need to manually enter
            "Description": "Issue key",  # dynamic parameter // jira issue key
            "Cost": "15000",  # dynamic parameter / from Jira
            "CitySender": "8d5a980d-391c-11dd-90d9-001a92567626",
            "Sender": "fdc96d91-77e0-11e9-9937-005056881c6b",
            "SenderAddress": "590fa4bd-7e8a-11ec-8513-b88303659df5",
            "ContactSender": "eaeec46f-ea91-11ee-a60f-48df37b921db",
            "SendersPhone": "380977456220",
            "CityRecipient": 'city',  # dynamic parameter
            "Recipient": 'recipient',  # dynamic parameter
            "RecipientAddress": 'recipient_address',  # dynamic parameter // can be warehouse or address
            "ContactRecipient": 'contact_recipient',  # dynamic parameter
            "RecipientsPhone": 'phone'  # dynamic parameter
        }
    }
