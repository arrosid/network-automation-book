from napalm_base import get_network_driver

driver = get_network_driver("ios")
ios_r1 = driver("192.168.99.1","user","user123")
ios_r1.open()

r1_facts = ios_r1.get_facts()
print r1_facts

ios_r1.close()
