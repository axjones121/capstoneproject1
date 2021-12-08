-- from the terminal run:
-- psql < newsapp.sql
DROP DATABASE IF EXISTS newsapp_capstone;

CREATE DATABASE newsapp_capstone;

\c newsapp_capstone


-- make sure that there are semicolons
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    image TEXT NOT NULL,
    url TEXT NOT NULL,
    read BOOLEAN DEFAULT 'f'
);


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(25) UNIQUE NOT NULL,
    password VARCHAR(70) NOT NULL,
    article_id INTEGER REFERENCES articles(id)
);




CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    comment TEXT,
    article_id INTEGER NOT NULL REFERENCES articles(id)
);






  
INSERT INTO articles 
  (title, description, image, url)
VALUES
  ('Ancient artifact found at bottom of sea', 'Ancient artifact found at the bottom of the sea of Italian item dated to be 2000 years old. This artifact holds clues the lost technology of the ancient greek civilization', 'https://static1.thetravelimages.com/wordpress/wp-content/uploads/2018/09/underwater-6.png' ,'www.google.com/artifact'),
  ('Colombian beetles exported to Japan with help from cryptocurrency - Reuters', 'TUNJA, Colombia Nov 4 (Reuters) - A Colombian exporter of long-horned beetles, a popular pet for Japanese children, has created its own cryptocurrency to avoid high commissions on international sales. "It''s an alternative to be able to export the beetles to Japan or any other part of the world and be able to use it as a method of payment," said Carmelo Campos, chief programmer of Tierra Viva, based in the central Andean city of Tunja.', 'https://www.reuters.com/resizer/2q5zRf33HiyM4kWqmX4l3JfN3DE=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/2A5Y42P4NJM7NPU7Q2UH56T4IQ.jpg', 'https://www.reuters.com/technology/colombian-beetles-exported-japan-with-help-cryptocurrency-2021-11-04/'),
  ('Election results updates: NJ Senate president loses in stunning upset; Atlanta mayoral runoff set', 'Election results continued to become finalized on Thursday, two days after Election Day. At midday, the Associated Press called the race of New Jersey''s state Senate president – and he lost. New Jersey does not have an automatic recount law, but the candidates are permitted to request one. The party that wants a recount has to file a suit in State Superior Court in the counties where they want to contest tallies. That has to be done within 17 days of Election Day.In Virginia, Republican Glenn Youngkin won the race to become the next governor on Tuesday. A businessman turned politician, Youngkin defeated Democrat and former Gov. Terry McAuliffe in a come-from-behind win. In fact, Republicans dominated statewide races in Virginia.Michelle Wu became the first elected female mayor of Boston and Democrat Eric Adams was elected New York’s second Black mayor, while Alvin Bragg became Manhattan’s first Black district attorney.', 'https://www.minnpost.com/wp-content/uploads/2021/11/PhilMurphy2021ElectionNight940.png?strip=all', 'https://www.usatoday.com/story/news/politics/2021/11/03/election-results-2021-live-updates-new-jersey/6263455001/');

INSERT INTO users
  (username, password)
VALUES
  ('Dokie2027', 'j123lj4123jk4j123kj41k23j4');  

  -- rememeber to put in the semicolons
-- do not forget the commas and the semicolon at the end
-- refer to 24.4.8