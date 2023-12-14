DO $$ 
BEGIN
    IF EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'users' and table_schema = 'raw') THEN
        DROP TABLE raw.users;
    END IF;
    CREATE TABLE raw.users (
        user_id UUID PRIMARY KEY,
        seed VARCHAR,
        gender VARCHAR,
        name JSONB,
        location JSONB,
        email VARCHAR,
        login JSONB,
        dob JSONB,
        registered JSONB,
        phone VARCHAR,
        cell VARCHAR,
        id JSONB,
        picture JSONB,
        nat VARCHAR
    );
END $$;