-- SWAMI KARUPPASWAMI THUNNAI

create database rest;

use rest;


create table if not exists client_credential(
    id bigint primary key auto_increment,
    email varchar(100) unique key,
    password char(60) not null,
    name text not null,
    verified tinyint(1) default 0 not null
);

