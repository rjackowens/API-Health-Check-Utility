master = {
    "environment" : {
        1: "https://DEV-01:443/",
        2: "https://DEV-01:443/",
        3: "https://QA-01:443/",
        4: "https://QA-01:443/",
        5: "https://PROD-01:443/",
        6: "https://PROD-01:443/",
        },
    "service" : {
        1: "AuthenticationService",
        2: "CommissionsService",
        3: "ConfigurationService",
        4: "CustomerService",
        5: "DistributorService",
        6: "EquipmentService",
        7: "EventService",
        8: "FieldRepService",
        9: "FileHandlerService",
        10: "LaunchPadService",
        11: "OrderService",
        12: "PartsService",
        13: "ReportingService",
        14: "UnderwritingService",
        15: "UserService"
        },
    "globalendpoint" : {
        "Version": "/X",
        "Health": "/X"
        },
    "authentication" : {
        "Login": "/X",
        "Logout": "/X,
        "Version": "/X,
        "Health": "/X"
        },
    "commissions" : {
        "Requests": "/X",
        "Tests": "/X",
        "Sent": "/X",
        "Version": "/X",
        "Health": "/X"
        },
    "configuration" : {
        "Version": "/X",
        "Health": "/X"
        },
    "customer" : {
        "Addresses": "/X",
        "Version": "/X",
        "Health": "/X"
        },
    "distributor" : {
        "List": "/X",
        "Version": "/X",
        "Health": "/X"
        },
    "equipment" : {
        "Statuses": "/X",
        "Specials": "/X",
        "Categories": "/X",
        "Types": "/X",
        "Index": "/X",
        "Listings": "/X",
        "Tests": "/X",
        "Version": "/X",
        "Health": "/X"
        },
    "fieldrep" : {
        "List": "/X",
        "Version": "/X",
        "Health": "/X"        
        },
    "filehandler" : {
        "List": "/X",
        "Index": "/X",
        "Version": "/X",
        "Health": "/X"
        },
    "launchpad" : {
        "Version": "/X",
        "Health": "/X"
        },
    "parts" : {
        "List": "/X",
        "Numbers": "/X",
        "Version": "/X",
        "Health": "/X"
        },
    "reporting" : {
        "Reports": "/X",
        "Views": "/X",
        "Version": "/X",
        "Health": "/X"
        },
    "user" : {
        "Groups": "/X",
        "Notifications": "/X",
        "User": "/X",
        "Version": "//X",
        "Health": "/X"
        },
    }
