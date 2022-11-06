


INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (1, gen_random_uuid(), 'SoS #1');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (2, gen_random_uuid(), 'SoS #2');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (3, gen_random_uuid(), 'SoS #3');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (4, gen_random_uuid(), 'SoS #4');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (5, gen_random_uuid(), 'SoS #5');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (6, gen_random_uuid(), 'SoS #6');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (7, gen_random_uuid(), 'SoS #7');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (8, gen_random_uuid(), 'SoS #8');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (9, gen_random_uuid(), 'SoS #9');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (10, gen_random_uuid(), 'SoS #10');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (11, gen_random_uuid(), 'SoS #11');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (12, gen_random_uuid(), 'SoS #12');
INSERT INTO sos (sos_id, sos_external_id, sos_name) VALUES (13, gen_random_uuid(), 'SoS #13');
SELECT setval(pg_get_serial_sequence('sos', 'sos_id'), COALESCE(MAX(sos_id), 1), MAX(sos_id) IS NOT null) FROM sos;


INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 1 , gen_random_uuid(), 'Battery storages');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 2 , gen_random_uuid(), 'Electric Load');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 3 , gen_random_uuid(), 'Photovoltaic System');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 4 , gen_random_uuid(), 'Wind Energy system');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 5 , gen_random_uuid(), '(Prosumers) Households with Photovoltaic cells and wind turbines');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 6 , gen_random_uuid(), 'charging station for electric vehicles');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 7 , gen_random_uuid(), 'Transmission line');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 8 , gen_random_uuid(), 'Transformer');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 9 , gen_random_uuid(), 'Building Management System (BMS)');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 10 , gen_random_uuid(), 'Heating/Ventilation and Air-Conditioning system (HVAC)');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 11 , gen_random_uuid(), 'Lighting CS');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 12 , gen_random_uuid(), 'Smart Grid CS');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 13 , gen_random_uuid(), 'Audiovisual Management CS');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 14 , gen_random_uuid(), 'Online Scheduling CS');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 15 , gen_random_uuid(), 'Fire Detection CS');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 16 , gen_random_uuid(), 'Security Surveillance CS');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 17 , gen_random_uuid(), 'Emergency Management CS');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 18 , gen_random_uuid(), 'distributed traffic lights network');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 19 , gen_random_uuid(), 'electric vehicles');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 20 , gen_random_uuid(), 'smart home applications utilizing IoT technologies');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 21 , gen_random_uuid(), 'one heating system');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 22 , gen_random_uuid(), 'one home automation system');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 23 , gen_random_uuid(), 'one vehicle parking system');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 24 , gen_random_uuid(), 'Virtual Power Plant (VPP) - Generator units/Controllable loads/Storage systems');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 25 , gen_random_uuid(), 'Market Agent');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 26 , gen_random_uuid(), 'Storage Agent');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 27 , gen_random_uuid(), 'Optimizer Agent');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 28 , gen_random_uuid(), 'Group (Representative) Agent - collectives');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 29 , gen_random_uuid(), 'Service providers');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 30 , gen_random_uuid(), 'Electric Appliances (lights/refrigerators/freezers/washers/dyers/water heaters/baseload)');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 31 , gen_random_uuid(), 'Central controller');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 32 , gen_random_uuid(), 'Diesel Generator Agent');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 33 , gen_random_uuid(), 'Sensors');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 34 , gen_random_uuid(), 'Transfer Switch');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 35 , gen_random_uuid(), 'IT Servers');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 36 , gen_random_uuid(), 'Cooling System');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 37 , gen_random_uuid(), 'Thermal Storage Device (TES)');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 38 , gen_random_uuid(), 'Power Distribution Unit (PDU)');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 39 , gen_random_uuid(), 'Water supply system (prosumer)');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 40 , gen_random_uuid(), 'Oil & gas supply sytem (prosumer)');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 41 , gen_random_uuid(), 'Transportation system (prosumer)');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 42 , gen_random_uuid(), 'provider of raw material');
INSERT INTO constituent (constituent_id, constituent_external_id, constituent_name) VALUES ( 43 , gen_random_uuid(), 'Commercial Greenhouse Growers (CGGs)');
SELECT setval(pg_get_serial_sequence('constituent', 'constituent_id'), COALESCE(MAX(constituent_id), 1), MAX(constituent_id) IS NOT null) FROM constituent;


INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 1 , gen_random_uuid(), 'supply the power to the electric grid if the output power of renewable sources decreased');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 2 , gen_random_uuid(), 'store energy back from the main grid in case of a grid-connected microgrid');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 3 , gen_random_uuid(), 'store energy back from the renewable energy sources if there excess of power');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 4 , gen_random_uuid(), 'capture the dynamic of the highly variable load');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 5 , gen_random_uuid(), 'generates energy from irradiance');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 6 , gen_random_uuid(), 'converts wind velocity into electrical energy using aerodynamic techniques');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 7 , gen_random_uuid(), 'use the energy locally');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 8 , gen_random_uuid(), 'Provide power to the village');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 9 , gen_random_uuid(), 'optimize light timing according to traffic flow');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 10 , gen_random_uuid(), 'initial random light pattern');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 11 , gen_random_uuid(), 'Automatically control the heaters, ventilators and air conditioners through temperature and the exchange of HVAC related information such as temperature and CO2 levels');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 12 , gen_random_uuid(), 'Automatically control the lights according to the occupancy and/or the outside brightness information');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 13 , gen_random_uuid(), 'Manage the energy through energy controlling actions to keep the balance between the energy production and consumption ');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 14 , gen_random_uuid(), 'send energy alerts to the Emergency Management CS in case of power outage');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 15 , gen_random_uuid(), 'Manage the screen projectors by adjusting the brightness to the needed level based on the type of the projection and the room brightness information');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 16 , gen_random_uuid(), 'Manage the online booking');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 17 , gen_random_uuid(), 'broadcast the booking information to the other CSs to adjust the lights, HVAC and audiovisual systems');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 18 , gen_random_uuid(), 'Detect automatically the fire in the building through fire alarms');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 19 , gen_random_uuid(), 'notify the BMS and security surveillance CSs to execute necessary emergency actions');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 20 , gen_random_uuid(), 'Manage the access in the smart building');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 21 , gen_random_uuid(), 'detect intruders');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 22 , gen_random_uuid(), 'send an intruder alert with the corresponding location to the Emergency Management CS to take the necessary emergency actions');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 23 , gen_random_uuid(), 'Manage the emergencies in the building based on the emergency alerts and by applying the corresponding emergency actions');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 24 , gen_random_uuid(), 'Charging of the EVs according to their battery state and pricing conditions');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 25 , gen_random_uuid(), 'charging algorithm based on price cap');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 26 , gen_random_uuid(), 'FIFO queue to charge');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 27 , gen_random_uuid(), 'parallel charging (1 hour per EV)');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 28 , gen_random_uuid(), 'Charging based on its energy');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 29 , gen_random_uuid(), 'consume energy while performing their missions');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 30 , gen_random_uuid(), 'warm the house');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 31 , gen_random_uuid(), 'take advantage from car heat if the last is parked in the garage');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 32 , gen_random_uuid(), 'Manage the interplay between the heating system, the garage sensor and port and the car detection sensor');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 33 , gen_random_uuid(), 'park inside or outside, depending on the weather conditions');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 34 , gen_random_uuid(), 'keep minimum temperature electrically when parked outside in very cold weather');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 35 , gen_random_uuid(), 'manages the participation of DERs and a VPP');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 36 , gen_random_uuid(), 'provides DERs with the information to access to the VPP');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 37 , gen_random_uuid(), 'receives the information about electricity that had been produced');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 38 , gen_random_uuid(), 'pays the cost of electricity production to the VPP using the proposed policy');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 39 , gen_random_uuid(), 'manages DERs’ participation');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 40 , gen_random_uuid(), 'collects the information of electricity producede');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 41 , gen_random_uuid(), 'informs the collected expectation information and the collected production information to the grid');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 42 , gen_random_uuid(), 'distributes incomings from the grid to its DERs using the proposed policy');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 43 , gen_random_uuid(), 'participates in a smart grid and a VPP');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 44 , gen_random_uuid(), 'estimates its production');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 45 , gen_random_uuid(), 'generates electricity');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 46 , gen_random_uuid(), 'informs its own actual production and own expected production information to the VPP');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 47 , gen_random_uuid(), 'receives the incomings from the VPP');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 48 , gen_random_uuid(), 'produces electricity based on its power curve of electrical output for a given wind speed');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 49 , gen_random_uuid(), 'calculates future energy prices given predicted energy loads');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 50 , gen_random_uuid(), 'provides the storage facility to the prosumers');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 51 , gen_random_uuid(), 'performs demand-response optimization');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 52 , gen_random_uuid(), 'energy consumption and production');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 53 , gen_random_uuid(), 'interacts with the market, storage and optimizer agents to maximizes the benefits of its prosumers');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 54 , gen_random_uuid(), 'make local decisions');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 55 , gen_random_uuid(), 'aggregate the combined energy consumption/production of its prosumers');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 56 , gen_random_uuid(), 'optimize the load schedules of all prosumers together to optimize energy costs and/or to avoid use in energy peaks');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 57 , gen_random_uuid(), 'shift energy loads to off-peak hours');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 58 , gen_random_uuid(), 'store any excess generated power in battery storage');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 59 , gen_random_uuid(), 'sell the excess power back to the grid');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 60 , gen_random_uuid(), 'sell the excess power to other groups that are in need of power');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 61 , gen_random_uuid(), 'connected to the experiment through specific distributed agents');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 62 , gen_random_uuid(), 'deals with electricity prices (demand/response)');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 63 , gen_random_uuid(), 'responds to consumer demands (allow/block)');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 64 , gen_random_uuid(), 'calculates the new demand and total power');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 65 , gen_random_uuid(), 'offers  an uninterruptible source of electricity when all other resources of electricity fail');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 66 , gen_random_uuid(), 'In a power loss, controls the number of generators depending on the estimated amount of electricity needed');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 67 , gen_random_uuid(), 'transfers the electrical load back to the utility or the renewables and return generator to stand-by mode when the Smart Grid power is normal or renewables can meet the demand');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 68 , gen_random_uuid(), 'Feeds the database along with sensored data');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 69 , gen_random_uuid(), 'collect wind speed, solar irradiance, temperature, voltage, current, and frequency data from the real Smart Grid');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 70 , gen_random_uuid(), 'Performs a series of essential processing, in order to permit the proper operation of the Smart Grid and the smooth transition from the normal operation mode to the islanded mode');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 71 , gen_random_uuid(), 'covers the DC demand in case of an emergency or power shortage');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 72 , gen_random_uuid(), 'transfers the energy to the DC systems that have to consume it');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 73 , gen_random_uuid(), 'consumes energy from the grid but also can feed back and sell excess energy generated by local sources');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 74 , gen_random_uuid(), 'supply the essential DC systems in a case of a power outage');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 75 , gen_random_uuid(), 'acts as a filter on the DC power supply, regulating the electrical power that fed all the DC systems');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 76 , gen_random_uuid(), 'consume energy to execute the DC workload');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 77 , gen_random_uuid(), 'store cold coolant used to chill the air blown by the air conditioning units');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 78 , gen_random_uuid(), 'chills the server room and removes the heat produced by the IT servers');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 79 , gen_random_uuid(), 'Takes/Generate coolant from/to the TES, thus enhancing compressor operation and saving energy');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 80 , gen_random_uuid(), 'Powers (distributes the output filtered energy from the UPS) to  the IT servers and the cooling system');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 81 , gen_random_uuid(), 'provides infrastructure and exchanges goods and services (under pricing mechanisms)');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 82 , gen_random_uuid(), 'can serve as a through-transportation link, conveying resources to subsequent agents without performing production processes');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 83 , gen_random_uuid(), 'introduces new resources');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 84 , gen_random_uuid(), 'produces ornamental pot plants and vegetables');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 85 , gen_random_uuid(), 'time-shifts the use of artificial growth light from one hour to another');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 86 , gen_random_uuid(), 'employs a strategy for artificial lighting which adheres to production goals, while considering the request for LM from the VPP');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 87 , gen_random_uuid(), 'shifts light hours to perform load shifting or increase the number of light hours to perform valley filling');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 88 , gen_random_uuid(), 'minimization of generation cost');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 89 , gen_random_uuid(), 'profit maximization');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 90 , gen_random_uuid(), 'peak load reduction');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 91 , gen_random_uuid(), 'propagares changes in electric usage by end-use customers from their normal consumption patterns according to external factors');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 92 , gen_random_uuid(), 'LM requests: peak clipping, valley filling, and load shifting');
INSERT INTO basic_feature (feature_id, feature_external_id, description) VALUES ( 93 , gen_random_uuid(), 'applies its own decision making to make counter proposals to the CGGs, in cases where demand does not equal allocation.');
SELECT setval(pg_get_serial_sequence('basic_feature', 'feature_id'), COALESCE(MAX(feature_id), 1), MAX(feature_id) IS NOT null) FROM basic_feature;



INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 1 , gen_random_uuid(), 'load-generation balance');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 2 , gen_random_uuid(), 'control the battery and enhance the operation of the system');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 3 , gen_random_uuid(), 'decrease the power consumption from power utility by using available energy from the solar panels');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 4 , gen_random_uuid(), 'supply power power to the electric load');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 5 , gen_random_uuid(), 'supply power to homes even in the event of an electric grid outage');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 6 , gen_random_uuid(), 'to ensure the comfort of its occupants by enhancing the automation to relief them from manual control of different services while increasing the energy savings');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 7 , gen_random_uuid(), 'minimize the average vehicle waiting time in the network');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 8 , gen_random_uuid(), 'minimize the local waiting time for vehicles');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 9 , gen_random_uuid(), 'north-to-south, red-to-green transition times');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 10 , gen_random_uuid(), 'Optimize the overall charging behavior');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 11 , gen_random_uuid(), 'avoid many simultaneous charging cycles');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 12 , gen_random_uuid(), 'minimum peak loads emerging');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 13 , gen_random_uuid(), 'cost limits are not exceeded');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 14 , gen_random_uuid(), 'balance between energy production and consumption');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 15 , gen_random_uuid(), 'grid stability');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 16 , gen_random_uuid(), 'optimise energy usage in a range of weather conditions');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 17 , gen_random_uuid(), 'promote to use a VPP from a new electricity production cost policy');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 18 , gen_random_uuid(), 'cluster together into local energy collectives');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 19 , gen_random_uuid(), 'use storage and demand-response techniques');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 20 , gen_random_uuid(), 'balance energy consumption and production');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 21 , gen_random_uuid(), 'deploy batteries in different ways depending on the behaviour of their members');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 22 , gen_random_uuid(), 'market mechanisms');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 23 , gen_random_uuid(), 'battery storage models');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 24 , gen_random_uuid(), 'peak optimization');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 25 , gen_random_uuid(), 'demand side management');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 26 , gen_random_uuid(), 'energy consumption/production patterns');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 27 , gen_random_uuid(), 'distributed negotiations between groups');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 28 , gen_random_uuid(), 'Different responses according to different demand/response schemes (price-based)');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 29 , gen_random_uuid(), 'decision about the best control design of the Smart Grid');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 30 , gen_random_uuid(), 'optimizations of the decisions of the Smart Grid given the best control design');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 31 , gen_random_uuid(), 'to proactively plan the DC operation as a system to be able to exploit its latent flexible energy to achieve a deeper and more efficient integration with the local Smart Grid.');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 32 , gen_random_uuid(), 'to use as much as possible of the locally produced renewable energy and transact energy to decrease operational costs, optimizing its integration in smart grid advanced context.');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 33 , gen_random_uuid(), 'system disruption responses and minimization of  the overall costs of satisfying total demand from the system in these events');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 34 , gen_random_uuid(), 'agents perform different functions based on their unique advantages relative to other agents postdisruption');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 35 , gen_random_uuid(), 'coordination mechanism, dynamic reorganization and coordination of the network under a disruption');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 36 , gen_random_uuid(), 'Negotiation and collaboration for resource allocation and demand efficiency');
INSERT INTO emergent_behavior (emergent_id, emergent_external_id, description) VALUES ( 37 , gen_random_uuid(), 'Resolution of potencial conflicts');
SELECT setval(pg_get_serial_sequence('emergent_behavior', 'emergent_id'), COALESCE(MAX(emergent_id), 1), MAX(emergent_id) IS NOT null) FROM emergent_behavior;



INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (24, 13);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (43, 13);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (1, 11);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (32, 11);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (34, 11);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (26, 11);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (4, 11);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (35, 11);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (36, 11);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (37, 11);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (38, 11);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (5, 12);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (12, 12);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (39, 12);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (40, 12);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (41, 12);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (42, 12);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (9, 10);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (3, 10);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (4, 10);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (32, 10);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (12, 10);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (33, 10);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (31, 10);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (21, 9);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (10, 9);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (30, 9);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (31, 9);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (5, 8);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (25, 8);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (26, 8);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (27, 8);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (28, 8);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (29, 8);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (4, 7);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (12, 7);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (24, 7);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (21, 6);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (22, 6);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (23, 6);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (19, 5);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (20, 5);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (3, 4);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (19, 4);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (1, 1);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (2, 1);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (3, 1);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (4, 1);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (5, 1);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (6, 1);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (7, 1);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (8, 1);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (9, 2);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (10, 2);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (11, 2);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (12, 2);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (13, 2);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (14, 2);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (15, 2);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (16, 2);
INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (17, 2);

INSERT INTO constituent_sos (constituent_id, sos_id) VALUES (18, 3);
SELECT setval(pg_get_serial_sequence('constituent_sos', 'relation_id'), COALESCE(MAX(relation_id), 1), MAX(relation_id) IS NOT null) FROM constituent_sos;


INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (24, 88);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (24, 89);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (24, 90);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (24, 91);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (24, 92);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (24, 93);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (43, 84);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (43, 85);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (43, 86);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (43, 87);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (5, 81);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (5, 82);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (12, 81);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (12, 82);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (39, 81);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (39, 82);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (40, 81);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (40, 82);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (41, 81);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (41, 82);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (42, 83);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (42, 83);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (1, 74);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (1, 75);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (32, 71);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (34, 72);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (34, 73);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (26, 74);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (26, 75);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (35, 76);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (36, 78);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (36, 79);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (36, 77);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (37, 77);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (38, 80);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (9, 64);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (32, 65);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (12, 66);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (12, 67);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (12, 68);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (33, 69);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (31, 70);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (21, 29);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (10, 29);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (30, 29);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (31, 62);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (31, 63);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (12, 35);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (12, 36);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (12, 37);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (12, 38);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (24, 39);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (24, 40);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (24, 41);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (24, 42);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (4, 43);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (4, 44);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (4, 45);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (4, 46);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (4, 47);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (4, 48);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (21, 30);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (21, 31);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (22, 32);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (23, 33);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (23, 34);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (19, 24);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (20, 29);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (19, 24);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (19, 25);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (19, 26);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (19, 27);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (19, 28);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (3, 25);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (3, 28);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (1, 1);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (1, 2);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (1, 3);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (2, 4);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (3, 5);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (4, 6);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (5, 7);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (6, 7);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (7, 8);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (8, 8);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (9, 9);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (10, 9);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (11, 10);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (12, 11);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (12, 12);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (13, 13);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (14, 14);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (14, 15);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (15, 16);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (15, 17);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (16, 18);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (16, 19);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (16, 20);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (17, 21);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (18, 22);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (18, 23);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (5, 52);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (28, 52);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (28, 53);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (28, 54);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (28, 55);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (28, 56);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (28, 57);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (28, 58);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (28, 59);
INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (28, 60);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (29, 61);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (25, 49);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (26, 50);

INSERT INTO constituent_basic_feature (constituent_id, basic_feature_id) VALUES (27, 51);
SELECT setval(pg_get_serial_sequence('constituent_basic_feature', 'relation_id'), COALESCE(MAX(relation_id), 1), MAX(relation_id) IS NOT null) FROM constituent_basic_feature;


INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (84, 36);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (85, 36);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (86, 36);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (87, 36);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (88, 36);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (89, 36);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (90, 36);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (91, 36);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (92, 36);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (93, 36);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (84, 37);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (85, 37);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (86, 37);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (87, 37);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (88, 37);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (89, 37);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (90, 37);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (91, 37);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (92, 37);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (93, 37);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (81, 33);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (82, 33);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (83, 33);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (81, 34);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (82, 34);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (83, 34);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (81, 35);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (82, 35);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (83, 35);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (29, 28);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (62, 28);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (63, 28);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (64, 29);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (65, 29);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (66, 29);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (67, 29);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (68, 29);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (69, 29);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (70, 29);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (5, 29);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (6, 29);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (71, 31);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (72, 31);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (73, 31);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (74, 31);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (75, 31);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (76, 31);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (77, 31);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (78, 31);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (79, 31);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (80, 31);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (6, 31);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (71, 32);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (72, 32);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (73, 32);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (74, 32);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (75, 32);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (76, 32);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (77, 32);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (78, 32);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (79, 32);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (80, 32);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (6, 32);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (64, 30);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (65, 30);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (66, 30);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (67, 30);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (68, 30);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (69, 30);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (70, 30);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (5, 30);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (6, 30);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (49, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (50, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (51, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (52, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (53, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (54, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (55, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (56, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (57, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (58, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (59, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (60, 27);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (61, 27);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (49, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (50, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (51, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (52, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (53, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (54, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (55, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (56, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (57, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (58, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (59, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (60, 26);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (61, 26);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (49, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (50, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (51, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (52, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (53, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (54, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (55, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (56, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (57, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (58, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (59, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (60, 25);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (61, 25);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (49, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (50, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (51, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (52, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (53, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (54, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (55, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (56, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (57, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (58, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (59, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (60, 24);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (61, 24);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (49, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (50, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (51, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (52, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (53, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (54, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (55, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (56, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (57, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (58, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (59, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (60, 23);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (61, 23);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (49, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (50, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (51, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (52, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (53, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (54, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (55, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (56, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (57, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (58, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (59, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (60, 22);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (61, 22);


INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (52, 18);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (52, 19);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (52, 20);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (52, 21);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (53, 21);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (54, 21);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (55, 21);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (56, 21);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (57, 21);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (58, 21);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (59, 21);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (60, 21);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (35, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (36, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (37, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (38, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (39, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (40, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (41, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (42, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (43, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (44, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (45, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (46, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (47, 17);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (48, 17);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (30, 16);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (31, 16);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (32, 16);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (33, 16);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (34, 16);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (24, 10);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (24, 11);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (24, 12);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (24, 13);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (29, 10);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (29, 11);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (29, 12);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (29, 13);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (5, 14);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (5, 15);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (24, 14);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (24, 15);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (25, 14);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (25, 15);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (26, 14);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (26, 15);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (27, 14);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (27, 15);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (28, 14);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (28, 15);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (4, 1);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (5, 1);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (6, 1);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (1, 2);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (2, 2);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (3, 2);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (4, 2);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (5, 2);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (6, 2);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (7, 2);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (8, 2);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (1, 3);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (2, 3);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (3, 3);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (4, 3);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (5, 3);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (6, 3);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (7, 3);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (8, 3);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (1, 4);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (2, 4);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (3, 4);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (4, 4);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (5, 4);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (6, 4);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (7, 4);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (8, 4);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (1, 5);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (2, 5);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (3, 5);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (4, 5);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (5, 5);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (6, 5);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (7, 5);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (8, 5);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (9, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (10, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (11, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (12, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (13, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (14, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (15, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (16, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (17, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (18, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (19, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (20, 6);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (21, 6);

INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (22, 7);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (22, 8);
INSERT INTO basic_feature_emergent_behavior (basic_feature_id, emergent_behavior_id) VALUES (23, 9);
SELECT setval(pg_get_serial_sequence('basic_feature_emergent_behavior', 'relation_id'), COALESCE(MAX(relation_id), 1), MAX(relation_id) IS NOT null) FROM basic_feature_emergent_behavior;


INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (31, 11);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (32, 11);

INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (33, 12);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (34, 12);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (35, 12);

INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (36, 13);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (37, 13);

INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (28, 9);

INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (17, 7);

INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (16, 6);

INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (29, 10);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (30, 10);

INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (10, 5);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (11, 5);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (12, 5);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (13, 5);

INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (1, 1);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (2, 1);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (3, 1);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (4, 1);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (5, 1);

INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (6, 2);

INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (7, 3);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (8, 3);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (9, 3);

INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (14, 4);
INSERT INTO sos_emergent_behavior (emergent_behavior_id, sos_id) VALUES (15, 4);
SELECT setval(pg_get_serial_sequence('sos_emergent_behavior', 'relation_id'), COALESCE(MAX(relation_id), 1), MAX(relation_id) IS NOT null) FROM sos_emergent_behavior;
