from Streamo import db, app
from Streamo.models import Movies_Show
from datetime import date

with app.app_context():
    wicked = Movies_Show('Wicked','Musical','Elphaba, misunderstood because of her green skin, forges an unlikely friendship with popular student Galinda at Shiz University in the Land of Oz.',date(2024,12,22),160,'static/posters/wicked.png')
    office = Movies_Show('The Office','Comedy',"Led by the comically incompetent Michael Scott, employees plod along at Dunder Mifflin's Scranton-based paper supply branch, where foibles, feuds and office romances unfold through the lens of an ever-present documentary crew.",date(2005,3,24),30,'static/posters/office.png')
    house = Movies_Show('House','Drama','Prickly anti-hero Dr. Gregory House wields flawless instincts and unconventional thinking to tackle health mysteries with brutal honesty.',date(2004,11,16),60,'static/posters/house.png')
    years = Movies_Show('The Last Five Years','Musical','In New York, a struggling actress and a successful writer sing about their failed marriage from two perspectives.',date(2014,9,7),94,'static/posters/years.png')
    macbeth = Movies_Show('Macbeth','Drama','After murdering King Duncan and seizing the throne, Macbeth becomes consumed with guilt and paranoia as the tyrannical ruler of Scotland.',date(2015,10,2),113,'static/posters/macbeth.png')
    sonic = Movies_Show('Sonic The Hedgehog','Kids',"Powered with incredible speed, Sonic races across the globe to stop uncool evil genius Dr. Robotnik from achieving world domination.",date(2020,2,12),98,'static/posters/sonic.png')
    sonic2 = Movies_Show('Sonic The Hedgehog 2','Kids',"After settling in Green Hills, Sonic is eager to prove that he has what it takes to be a true hero. His test comes when Dr. Robotnik returns with a new partner, Knuckles, in search of a mystical emerald that has the power to destroy civilizations. Sonic teams up with his own sidekick, Tails, and together they embark on a globe-trotting journey to find the emerald before it falls into the wrong hands.",date(2022,4,8),122,'static/posters/sonic2.png')
    sonic3 = Movies_Show('Sonic The Hedgehog 3','Kids',"Sonic, Knuckles and Tails reunite to battle Shadow, a mysterious new enemy with powers unlike anything they've faced before. With their abilities outmatched in every way, they seek out an unlikely alliance to stop Shadow and protect the planet.",date(2024,12,20),109,'static/posters/sonic3.png')
    nosferatu = Movies_Show('Nosferatu','Horror','An ancient Transylvanian vampire becomes obsessed with a haunted young woman in 19th-century Germany, causing untold horror in its wake.',date(2024,12,25),136,'static/posters/nosferatu.png')
    invisible = Movies_Show('The Invisible Man','Horror','When a woman returns to the home of her scientist ex-boyfriend after he commits suicide, she experiences strange terrors and happening.',date(2020,2,28),124,'static/posters/invisible.png')

    
    db.session.add_all([wicked,office,house,years,macbeth,sonic,sonic2,sonic3,nosferatu,invisible])
    db.session.commit()