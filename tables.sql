-- Create Database (if not exists)
CREATE DATABASE IF NOT EXISTS my_database;
USE my_database;

-- Create Countries Table
CREATE TABLE IF NOT EXISTS Countries (
    id CHAR(2) PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Cities (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    country_id CHAR(2),
    FOREIGN KEY (country_id) REFERENCES Countries(id)
);

-- Create Users Table
CREATE TABLE IF NOT EXISTS Users (
    id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create Places Table
CREATE TABLE IF NOT EXISTS Places (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    city_id INTEGER,
    user_id VARCHAR(36),
    FOREIGN KEY (city_id) REFERENCES Cities(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Create Amenities Table
CREATE TABLE IF NOT EXISTS Amenities (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

-- Create Place_Amenities Table (Many-to-Many Relationship)
CREATE TABLE IF NOT EXISTS Place_Amenities (
    place_id INTEGER,
    amenity_id INTEGER,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES Places(id),
    FOREIGN KEY (amenity_id) REFERENCES Amenities(id)
);

-- Ensure all changes are committed
COMMIT;
