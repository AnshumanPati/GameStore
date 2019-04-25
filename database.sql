DROP TABLE IF EXISTS `users`;


CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL auto_increment,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(100) NOT NULL,
  `street` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `zipcode` int(6) NOT NULL,
  PRIMARY KEY (`username`),
  KEY(`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10001 DEFAULT CHARSET=latin1;

select * from users;

DROP TABLE IF EXISTS `products`;
create table `products`(`id` int primary key, `pName` varchar(50), `category` varchar(10), `description` varchar(30), `developer` varchar(30), `price` int, `rating` int, `available` int, `picture` varchar(30));
insert into products values(101,"FIFA 14","pc","Sports","Electronic Arts",999,4.3,5,"fifa14.jpg");
insert into products values(102,"FIFA 14","xbox","Sports","Electronic Arts",1499,4.3,5,"fifa14.jpg");
insert into products values(103,"FIFA 14","ps4","Sports","Electronic Arts",1499,4.3,5,"fifa14.jpg");
insert into products values(104,"FIFA 15","pc","Sports","Electronic Arts",999,4.2,5,"fifa15.jpg");
insert into products values(105,"FIFA 15","xbox","Sports","Electronic Arts",1499,4.2,5,"fifa15.jpg");
insert into products values(106,"FIFA 15","ps4","Sports","Electronic Arts",1499,4.2,5,"fifa15.jpg");
insert into products values(107,"FIFA 16","pc","Sports","Electronic Arts",999,4.6,5,"fifa16.jpg");
insert into products values(108,"FIFA 16","xbox","Sports","Electronic Arts",1499,4.6,5,"fifa16.jpg");
insert into products values(109,"FIFA 16","ps4","Sports","Electronic Arts",1499,4.6,5,"fifa16.jpg");
insert into products values(110,"FIFA 17","pc","Sports","Electronic Arts",1499,4.3,5,"fifa17.jpg");
insert into products values(111,"FIFA 17","xbox","Sports","Electronic Arts",1999,4.3,5,"fifa17.jpg");
insert into products values(112,"FIFA 17","ps4","Sports","Electronic Arts",1999,4.6,5,"fifa17.jpg");
insert into products values(113,"FIFA 18","pc","Sports","Electronic Arts",2499,4.6,5,"fifa18.jpg");
insert into products values(114,"FIFA 18","xbox","Sports","Electronic Arts",2499,4.3,5,"fifa18.jpg");
insert into products values(115,"FIFA 18","ps4","Sports","Electronic Arts",2499,4.5,5,"fifa18.jpg");
insert into products values(116,"FIFA 19","pc","Sports","Electronic Arts",3499,4.3,5,"fifa19.jpg");
insert into products values(117,"FIFA 19","xbox","Sports","Electronic Arts",3499,4.3,5,"fifa19.jpg");
insert into products values(118,"FIFA 19","ps4","Sports","Electronic Arts",3499,4.3,5,"fifa19.jpg");
insert into products values(119,"Madden NFL 13","pc","Sports","Electronic Arts",1499,4.3,5,"nfl13.jpg");
insert into products values(120,"Madden NFL 13","xbox","Sports","Electronic Arts",1999,4.2,5,"nfl13.jpg");
insert into products values(121,"Madden NFL 13","ps4","Sports","Electronic Arts",1999,4.1,5,"nfl13.jpg"); 
insert into products values(122,"Madden NFL 14","pc","Sports","Electronic Arts",1499,4.1,5,"nfl14.jpg");
insert into products values(123,"Madden NFL 14","xbox","Sports","Electronic Arts",1999,4.0,5,"nfl14.jpg");
insert into products values(124,"Madden NFL 14","ps4","Sports","Electronic Arts",1999,4.0,5,"nfl14.jpg"); 
insert into products values(125,"Madden NFL 15","pc","Sports","Electronic Arts",1499,4.0,5,"nfl15.jpg");
insert into products values(126,"Madden NFL 15","xbox","Sports","Electronic Arts",1999,4.3,5,"nfl15.jpg");
insert into products values(127,"Madden NFL 15","ps4","Sports","Electronic Arts",1999,4.3,5,"nfl15.jpg"); 
insert into products values(128,"Madden NFL 16","pc","Sports","Electronic Arts",1499,4.3,5,"nfl16.jpg");
insert into products values(129,"Madden NFL 16","xbox","Sports","Electronic Arts",1999,4.3,5,"nfl16.jpg");
insert into products values(130,"Madden NFL 16","ps4","Sports","Electronic Arts",1999,4.3,5,"nfl16.jpg"); 
insert into products values(131,"Madden NFL 17","pc","Sports","Electronic Arts",2499,4.4,5,"nfl17.jpg");
insert into products values(132,"Madden NFL 17","xbox","Sports","Electronic Arts",2999,4.1,5,"nfl17.jpg");
insert into products values(133,"Madden NFL 17","ps4","Sports","Electronic Arts",2999,4.1,5,"nfl17.jpg"); 
insert into products values(134,"Madden NFL 18","pc","Sports","Electronic Arts",2499,4.1,5,"nfl18.jpg");
insert into products values(135,"Madden NFL 18","xbox","Sports","Electronic Arts",2999,4.2,5,"nfl18.jpg");
insert into products values(136,"Madden NFL 18","ps4","Sports","Electronic Arts",2999,4.1,5,"nfl18.jpg");
insert into products values(137,"Madden NFL 19","pc","Sports","Electronic Arts",2499,4.7,5,"nfl19.jpg");
insert into products values(138,"Madden NFL 19","xbox","Sports","Electronic Arts",2999,4.7,5,"nfl19.jpg");
insert into products values(139,"Madden NFL 19","ps4","Sports","Electronic Arts",2999,4.7,5,"nfl19.jpg");
insert into products values(140,"NBA Live 13","pc","Sports","Electronic Arts",1499,4.3,5,"nbalive13.jpg");
insert into products values(141,"NBA Live 13","xbox","Sports","Electronic Arts",1999,4.3,5,"nbalive13.jpg");
insert into products values(142,"NBA Live 13","ps4","Sports","Electronic Arts",1999,4.4,5,"nbalive13.jpg");
insert into products values(143,"NBA Live 14","pc","Sports","Electronic Arts",1499,4.4,5,"nbalive14.jpg");
insert into products values(144,"NBA Live 14","xbox","Sports","Electronic Arts",1999,4.3,5,"nbalive14.jpg");
insert into products values(145,"NBA Live 14","ps4","Sports","Electronic Arts",1999,4.4,5,"nbalive14.jpg");
insert into products values(146,"NBA Live 15","pc","Sports","Electronic Arts",1499,4.3,5,"nbalive15.jpg");
insert into products values(147,"NBA Live 15","xbox","Sports","Electronic Arts",1999,4.4,5,"nbalive15.jpg");
insert into products values(148,"NBA Live 15","ps4","Sports","Electronic Arts",1999,4.4,5,"nbalive15.jpg");
insert into products values(149,"NBA Live 16","pc","Sports","Electronic Arts",1499,4.3,5,"nbalive16.jpg");
insert into products values(150,"NBA Live 16","xbox","Sports","Electronic Arts",1999,4.0,5,"nbalive16.jpg");
insert into products values(151,"NBA Live 16","ps4","Sports","Electronic Arts",1999,4.1,5,"nbalive16.jpg");
insert into products values(152,"NBA Live 17","pc","Sports","Electronic Arts",2499,4.1,5,"nbalive17.jpg");
insert into products values(153,"NBA Live 17","xbox","Sports","Electronic Arts",2999,4.3,5,"nbalive17.jpg");
insert into products values(154,"NBA Live 17","ps4","Sports","Electronic Arts",2999,4.3,5,"nbalive17.jpg");
insert into products values(155,"NBA Live 18","pc","Sports","Electronic Arts",2499,4.2,5,"nbalive18.jpg");
insert into products values(156,"NBA Live 18","xbox","Sports","Electronic Arts",2999,4.3,5,"nbalive18.jpg");
insert into products values(157,"NBA Live 18","ps4","Sports","Electronic Arts",2999,4.3,5,"nbalive18.jpg");
insert into products values(158,"NBA Live 19","pc","Sports","Electronic Arts",2499,4.3,5,"nbalive19.jpg");
insert into products values(159,"NBA Live 19","xbox","Sports","Electronic Arts",2999,4.4,5,"nbalive19.jpg");
insert into products values(160,"NBA Live 19","ps4","Sports","Electronic Arts",2999,4.4,5,"nbalive19.jpg");
insert into products values(161,"NHL 13","pc","Sports","Electronic Arts",1499,4.1,5,"nhl13.jpg");
insert into products values(162,"NHL 13","xbox","Sports","Electronic Arts",1999,4.2,5,"nhl13.jpg");
insert into products values(163,"NHL 13","ps4","Sports","Electronic Arts",1999,4.2,5,"nhl13.jpg");
insert into products values(164,"NHL 14","pc","Sports","Electronic Arts",1499,4.4,5,"nhl14.jpg");
insert into products values(165,"NHL 14","xbox","Sports","Electronic Arts",1999,4.2,5,"nhl14.jpg");
insert into products values(166,"NHL 14","ps4","Sports","Electronic Arts",1999,4.2,5,"nhl14.jpg");  
insert into products values(167,"NHL 15","pc","Sports","Electronic Arts",1499,4.0,5,"nhl15.jpg");
insert into products values(168,"NHL 15","xbox","Sports","Electronic Arts",1999,4.2,5,"nhl15.jpg");
insert into products values(169,"NHL 15","ps4","Sports","Electronic Arts",1999,4.2,5,"nhl15.jpg");  
insert into products values(170,"NHL 16","pc","Sports","Electronic Arts",1499,4.1,5,"nhl16.jpg");
insert into products values(171,"NHL 16","xbox","Sports","Electronic Arts",1999,4.2,5,"nhl16.jpg");
insert into products values(172,"NHL 16","ps4","Sports","Electronic Arts",1999,4.2,5,"nhl16.jpg");  
insert into products values(173,"NHL 17","pc","Sports","Electronic Arts",1499,4.1,5,"nhl17.jpg");
insert into products values(174,"NHL 17","xbox","Sports","Electronic Arts",1999,4.2,5,"nhl17.jpg");
insert into products values(175,"NHL 17","ps4","Sports","Electronic Arts",1999,4.2,5,"nhl17.jpg");  
insert into products values(176,"NHL 18","pc","Sports","Electronic Arts",1499,3.8,5,"nhl18.jpg");
insert into products values(177,"NHL 18","xbox","Sports","Electronic Arts",1999,3.9,5,"nhl18.jpg");
insert into products values(178,"NHL 18","ps4","Sports","Electronic Arts",1999,3.8,5,"nhl18.jpg");  
insert into products values(179,"NHL 19","pc","Sports","Electronic Arts",1499,3.1,5,"nhl19.jpg");
insert into products values(180,"NHL 19","xbox","Sports","Electronic Arts",1999,3.2,5,"nhl19.jpg");
insert into products values(181,"NHL 19","ps4","Sports","Electronic Arts",1999,3.2,5,"nhl19.jpg");
insert into products values(182,"Pro Evolution Soccer 13","pc","Sports","Konami",499,4.1,5,"pes13.jpg");
insert into products values(183,"Pro Evolution Soccer 14","pc","Sports","Konami",499,4.1,5,"pes14.jpg");
insert into products values(184,"Pro Evolution Soccer 15","pc","Sports","Konami",999,4.1,5,"pes15.jpg");
insert into products values(185,"Pro Evolution Soccer 15","xbox","Sports","Konami",999,4.2,5,"pes15.jpg");
insert into products values(186,"Pro Evolution Soccer 15","ps4","Sports","Konami",999,4.2,5,"pes15.jpg"); 
insert into products values(187,"Pro Evolution Soccer 16","pc","Sports","Konami",999,4.1,5,"pes16.jpg");
insert into products values(188,"Pro Evolution Soccer 16","xbox","Sports","Konami",1499,4.2,5,"pes16.jpg");
insert into products values(189,"Pro Evolution Soccer 16","ps4","Sports","Konami",1499,4.2,5,"pes16.jpg");  
insert into products values(190,"Pro Evolution Soccer 17","pc","Sports","Konami",1499,4.1,5,"pes17.jpg");
insert into products values(191,"Pro Evolution Soccer 17","xbox","Sports","Konami",1999,4.2,5,"pes17.jpg");
insert into products values(192,"Pro Evolution Soccer 17","ps4","Sports","Konami",1999,4.2,5,"pes17.jpg");  
insert into products values(193,"Pro Evolution Soccer 18","pc","Sports","Konami",1499,4.1,5,"pes18.jpg");
insert into products values(194,"Pro Evolution Soccer 18","xbox","Sports","Konami",1999,4.2,5,"pes18.jpg");
insert into products values(195,"Pro Evolution Soccer 18","ps4","Sports","Konami",1999,4.2,5,"pes18.jpg");
insert into products values(196,"Pro Evolution Soccer 19","pc","Sports","Konami",1499,4.1,5,"pes19.jpg");
insert into products values(197,"Pro Evolution Soccer 19","xbox","Sports","Konami",1999,4.2,5,"pes19.jpg");
insert into products values(198,"Assassin's Creed","pc","Action","Ubisoft",499,4.7,5,"ac1.jpg");
insert into products values(199,"Assassin's Creed II","pc","Action","Ubisoft",799,4.9,5,"ac2.jpg");
insert into products values(200,"Assassin's Creed: Brotherhood","pc","Action","Ubisoft",999,4.7,5,"acb.jpg");
insert into products values(201,"Assassin's Creed: Revelations","pc","Action","Ubisoft",999,4.7,5,"acr.jpg");
insert into products values(202,"Assassin's Creed III","pc","Action","Ubisoft",1499,4.5,5,"ac3.jpg");
insert into products values(203,"Assassin's Creed IV: Black Flag","pc","Action","Ubisoft",1499,4.3,5,"ac4.jpg");
insert into products values(204,"Assassin's Creed IV: Black Flag","ps4","Action","Ubisoft",1999,4.3,5,"ac4.jpg");
insert into products values(205,"Assassin's Creed IV: Black Flag","pc","Action","Ubisoft",1999,4.3,5,"ac4.jpg");
insert into products values(206,"Assassin's Creed Unity","pc","Action","Ubisoft",1999,4.3,5,"ac5.jpg");
insert into products values(207,"Assassin's Creed Unity","xbox","Action","Ubisoft",1999,4.3,5,"ac5.jpg");
insert into products values(208,"Assassin's Creed Unity","ps4","Action","Ubisoft",1999,4.3,5,"ac5.jpg");
insert into products values(209,"Assassin's Creed Syndicate","pc","Action","Ubisoft",1999,4.7,5,"ac6.jpg");
insert into products values(210,"Assassin's Creed Syndicate","xbox","Action","Ubisoft",1999,4.7,5,"ac6.jpg");
insert into products values(211,"Assassin's Creed Syndicate","ps4","Action","Ubisoft",1999,4.7,5,"ac6.jpg");
insert into products values(212,"Assassin's Creed Rogue","pc","Action","Ubisoft",1999,4.3,5,"ac7.jpg");
insert into products values(213,"Assassin's Creed Rogue","xbox","Action","Ubisoft",1999,4.3,5,"ac7.jpg");
insert into products values(214,"Assassin's Creed Rogue","ps4","Action","Ubisoft",1999,4.3,5,"ac7.jpg");
insert into products values(215,"Assassin's Creed Origins","pc","Action","Ubisoft",2499,4.6,5,"ac8.jpg");
insert into products values(216,"Assassin's Creed Origins","xbox","Action","Ubisoft",2499,4.6,5,"ac8.jpg");
insert into products values(217,"Assassin's Creed Origins","ps4","Action","Ubisoft",2499,4.6,5,"ac8.jpg");
insert into products values(218,"Assassin's Creed Odyssey","pc","Action","Ubisoft",2499,4.7,5,"ac9.jpg");
insert into products values(219,"Assassin's Creed Odyssey","xbox","Action","Ubisoft",2499,4.7,5,"ac9.jpg");
insert into products values(220,"Assassin's Creed Odyssey","ps4","Action","Ubisoft",2499,4.7,5,"ac9.jpg");
insert into products values(221,"Tom Clancy's Rainbow Six Siege","pc","First-person shooter","Ubisoft",1499,4.4,5,"tcrss.jpg");
insert into products values(222,"Tom Clancy's Rainbow Six Siege","xbox","First-person shooter","Ubisoft",1499,4.4,5,"tcrss.jpg");
insert into products values(223,"Tom Clancy's Rainbow Six Siege","ps4","First-person shooter","Ubisoft",1499,4.4,5,"tcrss.jpg");
insert into products values(224,"Tom Clancy's Rainbow The Division","pc","Action","Ubisoft",1499,4.4,5,"tctd.jpg");
insert into products values(225,"Tom Clancy's Rainbow The Division","xbox","Action","Ubisoft",1499,4.4,5,"tctd.jpg");
insert into products values(226,"Tom Clancy's Rainbow The Division","ps4","Action","Ubisoft",1499,4.4,5,"tctd.jpg");
insert into products values(227,"Tom Clancy's Rainbow The Division 2","pc","Action","Ubisoft",1499,4.4,5,"tctd2.jpg");
insert into products values(228,"Tom Clancy's Rainbow The Division 2","xbox","Action","Ubisoft",1499,4.4,5,"tctd2.jpg");
insert into products values(229,"Tom Clancy's Rainbow The Division 2","ps4","Action","Ubisoft",1499,4.4,5,"tctd2.jpg");
insert into products values(230,"Far Cry 3","pc","Action","Ubisoft",1499,4.4,5,"fc3.jpg");
insert into products values(231,"Far Cry 4","pc","Action","Ubisoft",1999,4.7,5,"fc4.jpg");
insert into products values(232,"Far Cry 4","xbox","Action","Ubisoft",1999,4.7,5,"fc4.jpg");
insert into products values(233,"Far Cry 4","ps4","Action","Ubisoft",1999,4.7,5,"fc4.jpg");
insert into products values(234,"Far Cry 5","pc","Action","Ubisoft",1999,4.5,5,"fc5.jpg");
insert into products values(235,"Far Cry 5","xbox","Action","Ubisoft",1999,4.5,5,"fc5.jpg");
insert into products values(236,"Far Cry 5","ps4","Action","Ubisoft",1999,4.5,5,"fc5.jpg");
insert into products values(237,"Dark Souls","pc","Role-playing game","BANDAI NAMCO Entertainment",999,4.5,5,"ds.jpg");
insert into products values(238,"Dark Souls II","pc","Role-playing game","BANDAI NAMCO Entertainment",999,4.6,5,"ds2.jpg");
insert into products values(239,"Dark Souls II","xbox","Role-playing game","BANDAI NAMCO Entertainment",1499,4.6,5,"ds2.jpg");
insert into products values(240,"Dark Souls II","ps4","Role-playing game","BANDAI NAMCO Entertainment",1499,4.6,5,"ds2.jpg");
insert into products values(241,"Dark Souls III","pc","Role-playing game","BANDAI NAMCO Entertainment",1499,4.3,5,"ds3.jpg");
insert into products values(242,"Dark Souls III","xbox","Role-playing game","BANDAI NAMCO Entertainment",2499,4.3,5,"ds3.jpg");
insert into products values(243,"Dark Souls III","ps4","Role-playing game","BANDAI NAMCO Entertainment",2499,4.3,5,"ds3.jpg");
insert into products values(244,"The Witcher","pc","Role-playing game","CD Projekt Red",999,4.6,5,"thewitcher.jpg");
insert into products values(245,"The Witcher 2: Assassin of Kings","pc","Role-playing game","CD Projekt Red",999,4.6,5,"thewitcher2.jpg");
insert into products values(246,"The Witcher 2: Assassin of Kings","xbox","Role-playing game","CD Projekt Red",999,4.7,5,"thewitcher2.jpg");
insert into products values(247,"The Witcher 2: Assassin of Kings","ps4","Role-playing game","CD Projekt Red",999,4.7,5,"thewitcher2.jpg");
insert into products values(248,"The Witcher 3: The Wild Hunt","pc","Role-playing game","CD Projekt Red",1499,5.0,5,"thewitcher3.jpg");
insert into products values(249,"The Witcher 3: The Wild Hunt","xbox","Role-playing game","CD Projekt Red",1499,5.0,5,"thewitcher3.jpg");
insert into products values(250,"The Witcher 3: The Wild Hunt","ps4","Role-playing game","CD Projekt Red",1499,5.0,5,"thewitcher3.jpg");
insert into products values(251,"Red Dead Redemption 2","ps4","Action","Rockstar Games",1499,4.7,5,"rdr2.jpg");
insert into products values(252,"Red Dead Redemption 2","xbox","Action","Rockstar Games",1499,4.7,5,"rdr2.jpg");
insert into products values(253,"Grand Theft Auto V","xbox","Action","Rockstar Games",2499,4.7,5,"gta5.jpg");
insert into products values(254,"Grand Theft Auto V","ps4","Action","Rockstar Games",2499,4.7,5,"gta5.jpg");
insert into products values(255,"Grand Theft Auto V","pc","Action","Rockstar Games",2499,4.7,5,"gta5.jpg");
insert into products values(256,"Grand Theft Auto IV","pc","Action","Rockstar Games",2499,4.7,5,"gta4.jpg");
insert into products values(257,"The Sims 4","pc","Simulation","Electronic Arts",2499,4.7,5,"thesims4.jpg");
insert into products values(258,"The Last Of Us","ps4","Survival game","Sony CE",1999,4.5,5,"thelastofus.jpg");
insert into products values(259,"The Last Of Us 2","ps4","Survival game","Sony CE",2999,4.5,5,"thelastofus2.jpg");
insert into products values(260,"God Of War","pc","Action","Sony CE",1999,4.5,5,"gow.jpg");
insert into products values(261,"The Elder Scrolls IV: Oblivion","pc","Action","Bethesda Game Studios",999,4.5,5,"ec4.jpg");
insert into products values(262,"The Elder Scrolls V: Skyrim","pc","Action","Bethesda Game Studios",1999,4.5,5,"ec5.jpg");
insert into products values(263,"The Elder Scrolls V: Skyrim","ps4","Action","Bethesda Game Studios",1999,4.5,5,"ec5.jpg");
insert into products values(264,"The Elder Scrolls V: Skyrim","xbox","Action","Bethesda Game Studios",1999,4.5,5,"ec5.jpg");
insert into products values(265,"Need For Speed: Most Wanted","pc","Racing","Electronic Arts",999,4.5,5,"nfsmw.jpg");
insert into products values(266,"Need For Speed: Payback","pc","Racing","Electronic Arts",999,4.5,5,"nfsp.jpg");
insert into products values(267,"Need For Speed: Payback","ps4","Racing","Electronic Arts",999,4.5,5,"nfsp.jpg");
insert into products values(268,"Need For Speed: Payback","xbox","Racing","Electronic Arts",999,4.5,5,"nfsp.jpg");
insert into products values(269,"Need For Speed: No Limits","ps4","Racing","Electronic Arts",999,4.5,5,"nfsnl.jpg");
insert into products values(270,"Need For Speed: No Limits","pc","Racing","Electronic Arts",999,4.5,5,"nfsnl.jpg");
insert into products values(271,"Need For Speed: No Limits","xbox","Racing","Electronic Arts",999,4.5,5,"nfsnl.jpg");



select * from products;



DROP TABLE IF EXISTS `cart`;
CREATE TABLE IF NOT EXISTS `cart` (
  `uid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  PRIMARY KEY (`uid`,`pid`)
);

select * from cart;

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `orderid` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `pName` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  PRIMARY KEY (`orderid`)
) ENGINE=InnoDB AUTO_INCREMENT= 2000 DEFAULT CHARSET=latin1;

select * from orders;

