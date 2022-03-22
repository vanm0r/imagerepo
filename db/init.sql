create database images;
use images;
CREATE TABLE imagelinks (
  title VARCHAR(50),
  link VARCHAR(300),
  descr VARCHAR(200)
);
INSERT INTO imagelinks
  (title, link, descr)
VALUES
  ('Alaskan Husky', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/An_Alaskan_Husky_sked_dog_%28Quintin_Soloviev%29.jpg/1280px-An_Alaskan_Husky_sked_dog_%28Quintin_Soloviev%29.jpg', 'Image of the breed Alaskan Husky'),
  ('Beagle', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/MiloSmet.JPG/1280px-MiloSmet.JPG', 'Image of the breed Beagle');