--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.5
-- Dumped by pg_dump version 9.6.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: readings; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE readings (
    date timestamp without time zone DEFAULT now() NOT NULL,
    sensor real NOT NULL,
    api real NOT NULL,
    id integer NOT NULL
);


ALTER TABLE readings OWNER TO pi;

--
-- Name: readings_id_seq; Type: SEQUENCE; Schema: public; Owner: pi
--

CREATE SEQUENCE readings_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE readings_id_seq OWNER TO pi;

--
-- Name: readings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pi
--

ALTER SEQUENCE readings_id_seq OWNED BY readings.id;


--
-- Name: readings id; Type: DEFAULT; Schema: public; Owner: pi
--

ALTER TABLE ONLY readings ALTER COLUMN id SET DEFAULT nextval('readings_id_seq'::regclass);


--
-- Name: readings readings_pkey; Type: CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY readings
    ADD CONSTRAINT readings_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

