import whois

domain_name = input("Enter domain name : ")

whois_info = whois.whois(domain_name)


print("## Domain name information ##")

print("Domain name :", whois_info.domain_name)


print("\n## Informations Whois ##")

print("\nRegistrar :", whois_info.registrar)
print("\nServers name :", whois_info.name_servers)
print("\nCreation date :", whois_info.creation_date)
print("\nUpdated date :", whois_info.updated_date)
print("\nExpiration date :", whois_info.expiration_date)

server_number = 1

for name_server in whois_info.name_servers:
    print("## Information Serveur ", server_number, "##")

    whois_server = whois.whois(name_server)
    print("\nDomain name :", whois_server.domain_name)
    print("\nRegistrar :", whois_server.registrar)
    print("\nWhois Server :", whois_server.whois_server)
    print("\nCreation date :", whois_server.creation_date)
    if isinstance(whois_server.updated_date, list):
        print("\nUpdated date :", whois_server.updated_date[0])
    else:
        print("\nUpdated date :", whois_server.updated_date)
    print("\nExpiration date :", whois_server.expiration_date)
    print("\nName servers :", whois_server.name_servers)
    print("\nEmails :", whois_server.emails)
    print("\nDnssec :", whois_server.dnssec)
    print("\nName :", whois_server.name)
    print("\nOrg :", whois_server.org)
    print("\nAddress :", whois_server.address)
    print("\nCity :", whois_server.city)
    print("\nState :", whois_server.state)
    print("\nRegistrant postal code :", whois_server.registrant_postal_code)
    print("\nCountry :", whois_server.country)

    server_number += 1


print("\n## Owner Information ##")

print("Owner :", whois_info.name)
print("\nOwner emails :", whois_info.emails)
print("\nOrganization :", whois_info.organization)
print("\nCountry :", whois_info.country)