INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`, `permission`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com', 'Alan', 'Turing', 1);

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`, `permission`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com', 'Dennis', 'Ritchie', 0);

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`, `permission`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com', 'Leslie', 'Lamport',0);

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`, `permission`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com', 'Barbara', 'Liskov', 0);

/*
INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Apples', 'An edible cultivation of the Malus genus.', 2.00, 100, 'static/images/apple.jpeg', 'Fruit');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Bananas', 'A long curved fruit which grows in clusters and has soft pulpy flesh and yellow skin when ripe.', 1.00, 100, 'static/images/banana.jpeg', 'Fruit');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Mangos', 'The best fruit on the planet.', 4.00, 100, 'static/images/mango.jpeg', 'Fruit');
*/ 

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('1', 'aturing', '1', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('2', 'dritchie', '2', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('3', 'llamport', '3', 10, '2022-12-21 7:30:30', 5.50);
/*
INSERT into `inventory` (`make`, 'model' ,`mileage`, `price`, vin ,`color`, `image_url`, `body_style`)
VALUES ('car make', 'car model', XXXX , XXXX , XXXX ,color str, 'image path', 'vehichle type');

CREATE TABLE inventory(
    id INTEGER PRIMARY KEY NOT NULL,
    vin INTEGER NOT NULL,
    make VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL,
    mileage INTEGER NOT NULL,
    price INTEGER NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    body_style VARCHAR(255) NOT NULL
);

Begin new 'inventory' 
*/

/*-----------------
------Inventory----
*/-----------------

INSERT into `inventory` ( `vin`, `v_year`,`make`, `model`, `mileage` , `price` ,`image_url`, `body_style`)
VALUES ( 1234, 2022,'Ford', 'Ranger', 52, 38000,'static/images/FordRanger.jpeg', 'Truck');

INSERT into `inventory` ( `vin`, `v_year`,`make`, `model`, `mileage` , `price` ,`image_url`, `body_style`)
VALUES ( 2000, 2023,'Chevrolet', 'Silverado',  22, 60000,'static/images/ChevySilverado.jpeg', 'Truck');

INSERT into `inventory` ( `vin`, `v_year`,`make`, `model`, `mileage` , `price` ,`image_url`, `body_style`)
VALUES ( 7272, 2023,'Chevrolet', 'Malibu',  15, 33000,'static/images/ChevyMalibu.jpeg', 'Sedan');

INSERT into `inventory` ( `vin`, `v_year`,`make`, `model`, `mileage` , `price` ,`image_url`, `body_style`)
VALUES ( 7556, 2012,'Buick', 'Enclave', 72000, 23000,'static/images/BuickEnclave.jpeg', 'SUV');

INSERT into `inventory` (`vin`, `v_year`,`make`, `model`, `mileage` , `price` ,`image_url`, `body_style`)
VALUES ( 8045, 2022,'Chevrolet', 'Comaro',  15, 59000,'static/images/ChevroletComaro.jpeg', 'Coupe');

INSERT into `inventory` ( `vin`, `v_year`,`make`, `model`, `mileage` , `price` ,`image_url`, `body_style`)
VALUES ( 9876, 2023, 'Ford', 'Shelby GT500', 10, 88000,'static/images/FordShelbyGT500.jpeg', 'Coupe');

INSERT into `inventory` ( `vin`, `v_year`,`make`, `model`, `mileage` , `price` ,`image_url`, `body_style`)
VALUES ( 5050, 2023,'Chevrolet', 'Corvette',  12, 97000,'static/images/ChevyCorvette.jpeg', 'Coupe');




INSERT INTO `logs` (`type`, `message`, `log_time`)
VALUES ('INFO', 'Database initialized1', '2021-12-21 7:30:30');

INSERT INTO `logs` (`type`, `message`, `log_time`)
VALUES ('INFO', 'Database initialized21', '2021-12-21 7:30:30');

INSERT INTO `logs` (`type`, `message`, `log_time`)
VALUES ('INFO', 'Database initialized16', '2021-12-21 7:30:30');

INSERT INTO `logs` (`type`, `message`, `log_time`)
VALUES ('INFO', 'Database initialized134', '2021-12-21 7:30:30');