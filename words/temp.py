# This code was generated with the assistance of ChatGPT


# Sample input as a single string
input_string = """
about|𐑩𐑚𐑬𐑑
above|𐑩𐑚𐑳𐑝
abuse|𐑩𐑚𐑿𐑕
abuse|𐑩𐑚𐑿𐑟
accept|𐑩𐑒𐑕𐑧𐑐𐑑
accident|𐑨𐑒𐑕𐑦𐑛𐑩𐑯𐑑
accuse|𐑩𐑒𐑿𐑟
across|𐑩𐑒𐑮𐑪𐑕
activist|𐑨𐑒𐑑𐑦𐑝𐑦𐑕𐑑
actor|𐑨𐑒𐑑𐑼
admit|𐑩𐑛𐑥𐑦𐑑
adult|𐑨𐑛𐑳𐑤𐑑
advertise|𐑨𐑛𐑝𐑼𐑑𐑲𐑟
advise|𐑩𐑛𐑝𐑲𐑟
affect|𐑨𐑓𐑧𐑒𐑑
affect|𐑩𐑓𐑧𐑒𐑑
afraid|𐑩𐑓𐑮𐑱𐑛
after|𐑨𐑓𐑑𐑼
after|𐑭𐑓𐑑𐑼
again|𐑩𐑜𐑧𐑯
against|𐑩𐑜𐑧𐑯𐑕𐑑
agency|𐑱𐑡𐑩𐑯𐑕𐑦
agree|𐑩𐑜𐑮𐑰
airplane|𐑺𐑐𐑤𐑱𐑯
airport|𐑺𐑐𐑹𐑑
album|𐑨𐑤𐑚𐑩𐑥
alcohol|𐑨𐑤𐑒𐑩𐑣𐑪𐑤
alive|𐑩𐑤𐑲𐑝
almost|𐑷𐑤𐑥𐑴𐑕𐑑
alone|𐑩𐑤𐑴𐑯
along|𐑩𐑤𐑪𐑙
already|𐑷𐑤𐑮𐑧𐑛𐑦
although|𐑷𐑤𐑞𐑴
always|𐑷𐑤𐑢𐑱𐑟
amend|𐑩𐑥𐑧𐑯𐑛
among|𐑩𐑥𐑳𐑙
amount|𐑩𐑥𐑬𐑯𐑑
anarchy|𐑨𐑯𐑼𐑒𐑦
ancestor|𐑨𐑯𐑕𐑧𐑕𐑑𐑼
ancient|𐑱𐑯𐑗𐑩𐑯𐑑
anger|𐑨𐑙𐑜𐑼
animal|𐑨𐑯𐑦𐑥𐑩𐑤
announce|𐑩𐑯𐑬𐑯𐑕
another|𐑩𐑯𐑳𐑞𐑼
answer|𐑨𐑯𐑕𐑼
answer|𐑭𐑯𐑕𐑼
apologize|𐑩𐑐𐑪𐑤𐑩𐑡𐑲𐑟
appeal|𐑩𐑐𐑰𐑤
appear|𐑩𐑐𐑽
appoint|𐑩𐑐𐑶𐑯𐑑
approve|𐑩𐑐𐑮𐑵𐑝
argue|𐑸𐑜𐑿
around|𐑼𐑬𐑯𐑛
arrest|𐑼𐑧𐑕𐑑
arrive|𐑼𐑲𐑝
artillery|𐑸𐑑𐑦𐑤𐑼𐑦
assist|𐑩𐑕𐑦𐑕𐑑
astronaut|𐑨𐑕𐑑𐑮𐑩𐑯𐑷𐑑
astronomy|𐑩𐑕𐑑𐑮𐑪𐑯𐑩𐑥𐑦
asylum|𐑩𐑕𐑲𐑤𐑩𐑥
attach|𐑩𐑑𐑨𐑗
attack|𐑩𐑑𐑨𐑒
attempt|𐑩𐑑𐑧𐑥𐑐𐑑
attend|𐑩𐑑𐑧𐑯𐑛
attention|𐑩𐑑𐑧𐑯𐑖𐑩𐑯
autumn|𐑷𐑑𐑩𐑥
available|𐑩𐑝𐑱𐑤𐑩𐑚𐑩𐑤
average|𐑨𐑝𐑼𐑦𐑡
avoid|𐑩𐑝𐑶𐑛
awake|𐑩𐑢𐑱𐑒
award|𐑩𐑢𐑹𐑛
balance|𐑚𐑨𐑤𐑩𐑯𐑕
balloon|𐑚𐑩𐑤𐑵𐑯
ballot|𐑚𐑨𐑤𐑩𐑑
barrier|𐑚𐑨𐑮𐑽
battle|𐑚𐑨𐑑𐑩𐑤
beauty|𐑚𐑿𐑑𐑦
because|𐑚𐑦𐑒𐑪𐑟
become|𐑚𐑦𐑒𐑳𐑥
before|𐑚𐑦𐑓𐑹
begin|𐑚𐑦𐑜𐑦𐑯
behavior|𐑚𐑦𐑣𐑱𐑝𐑘𐑼
behind|𐑚𐑦𐑣𐑲𐑯𐑛
believe|𐑚𐑦𐑤𐑰𐑝
belong|𐑚𐑦𐑤𐑪𐑙
below|𐑚𐑦𐑤𐑴
betray|𐑚𐑦𐑑𐑮𐑱
better|𐑚𐑧𐑑𐑼
between|𐑚𐑦𐑑𐑢𐑰𐑯
biology|𐑚𐑲𐑪𐑤𐑩𐑡𐑦
black|𐑚𐑤𐑨𐑒
blame|𐑚𐑤𐑱𐑥
bleed|𐑚𐑤𐑰𐑛
blind|𐑚𐑤𐑲𐑯𐑛
block|𐑚𐑤𐑪𐑒
blood|𐑚𐑤𐑳𐑛
border|𐑚𐑹𐑛𐑼
borrow|𐑚𐑪𐑮𐑴
bottle|𐑚𐑪𐑑𐑩𐑤
bottom|𐑚𐑪𐑑𐑩𐑥
boycott|𐑚𐑶𐑒𐑪𐑑
brain|𐑚𐑮𐑱𐑯
brave|𐑚𐑮𐑱𐑝
bread|𐑚𐑮𐑧𐑛
break|𐑚𐑮𐑱𐑒
breathe|𐑚𐑮𐑰𐑞
bridge|𐑚𐑮𐑦𐑡
brief|𐑚𐑮𐑰𐑓
bright|𐑚𐑮𐑲𐑑
bring|𐑚𐑮𐑦𐑙
broadcast|𐑚𐑮𐑷𐑛𐑒𐑨𐑕𐑑
broadcast|𐑚𐑮𐑷𐑛𐑒𐑭𐑕𐑑
brother|𐑚𐑮𐑳𐑞𐑼
brown|𐑚𐑮𐑬𐑯
budget|𐑚𐑳𐑡𐑩𐑑
build|𐑚𐑦𐑤𐑛
building|𐑚𐑦𐑤𐑛𐑦𐑙
bullet|𐑚𐑫𐑤𐑩𐑑
burst|𐑚𐑻𐑕𐑑
business|𐑚𐑦𐑟𐑯𐑩𐑕
cabinet|𐑒𐑨𐑚𐑦𐑯𐑩𐑑
camera|𐑒𐑨𐑥𐑼𐑩
campaign|𐑒𐑨𐑥𐑐𐑱𐑯
cancel|𐑒𐑨𐑯𐑕𐑩𐑤
cancer|𐑒𐑨𐑯𐑕𐑼
candidate|𐑒𐑨𐑯𐑛𐑦𐑛𐑩𐑑
capital|𐑒𐑨𐑐𐑦𐑑𐑩𐑤
capture|𐑒𐑨𐑐𐑗𐑼
career|𐑒𐑼𐑽
careful|𐑒𐑺𐑓𐑩𐑤
carry|𐑒𐑨𐑮𐑦
catch|𐑒𐑨𐑗
cause|𐑒𐑷𐑟
ceasefire|𐑕𐑰𐑕𐑓𐑲𐑼
celebrate|𐑕𐑧𐑤𐑩𐑚𐑮𐑱𐑑
center|𐑕𐑧𐑯𐑑𐑼
century|𐑕𐑧𐑯𐑗𐑼𐑦
ceremony|𐑕𐑧𐑮𐑦𐑥𐑩𐑯𐑦
chairman|𐑗𐑺𐑥𐑩𐑯
champion|𐑗𐑨𐑥𐑐𐑾𐑯
chance|𐑗𐑨𐑯𐑕
chance|𐑗𐑭𐑯𐑕
change|𐑗𐑱𐑯𐑡
charge|𐑗𐑸𐑡
chase|𐑗𐑱𐑕
cheat|𐑗𐑰𐑑
cheer|𐑗𐑽
chemicals|𐑒𐑧𐑥𐑦𐑒𐑩𐑤𐑟
chemistry|𐑒𐑧𐑥𐑦𐑕𐑑𐑮𐑦
chief|𐑗𐑰𐑓
child|𐑗𐑲𐑤𐑛
children|𐑗𐑦𐑤𐑛𐑮𐑩𐑯
choose|𐑗𐑵𐑟
circle|𐑕𐑻𐑒𐑩𐑤
citizen|𐑕𐑦𐑑𐑦𐑟𐑩𐑯
civil|𐑕𐑦𐑝𐑩𐑤
civilian|𐑕𐑦𐑝𐑦𐑤𐑾𐑯
claim|𐑒𐑤𐑱𐑥
clash|𐑒𐑤𐑨𐑖
class|𐑒𐑤𐑨𐑕
class|𐑒𐑤𐑭𐑕
clean|𐑒𐑤𐑰𐑯
clear|𐑒𐑤𐑽
clergy|𐑒𐑤𐑻𐑡𐑦
climate|𐑒𐑤𐑲𐑥𐑩𐑑
climb|𐑒𐑤𐑲𐑥
clock|𐑒𐑤𐑪𐑒
close|𐑒𐑤𐑴𐑕
close|𐑒𐑤𐑴𐑟
cloth|𐑒𐑤𐑪𐑔
clothes|𐑒𐑤𐑴𐑞𐑟
cloud|𐑒𐑤𐑬𐑛
coalition|𐑒𐑴𐑩𐑤𐑦𐑖𐑩𐑯
coast|𐑒𐑴𐑕𐑑
coffee|𐑒𐑪𐑓𐑦
collapse|𐑒𐑩𐑤𐑨𐑐𐑕
collect|𐑒𐑩𐑤𐑧𐑒𐑑
collect|𐑒𐑪𐑤𐑧𐑒𐑑
college|𐑒𐑪𐑤𐑦𐑡
colony|𐑒𐑪𐑤𐑩𐑯𐑦
color|𐑒𐑳𐑤𐑼
combine|𐑒𐑩𐑥𐑚𐑲𐑯
combine|𐑒𐑪𐑥𐑚𐑲𐑯
command|𐑒𐑩𐑥𐑨𐑯𐑛
command|𐑒𐑩𐑥𐑭𐑯𐑛
comment|𐑒𐑪𐑥𐑧𐑯𐑑
committee|𐑒𐑩𐑥𐑦𐑑𐑦
common|𐑒𐑪𐑥𐑩𐑯
community|𐑒𐑩𐑥𐑿𐑯𐑦𐑑𐑦
company|𐑒𐑳𐑥𐑐𐑩𐑯𐑦
compare|𐑒𐑩𐑥𐑐𐑺
compete|𐑒𐑩𐑥𐑐𐑰𐑑
complete|𐑒𐑩𐑥𐑐𐑤𐑰𐑑
complex|𐑒𐑪𐑥𐑐𐑤𐑧𐑒𐑕
computer|𐑒𐑩𐑥𐑐𐑿𐑑𐑼
concern|𐑒𐑩𐑯𐑕𐑻𐑯
condemn|𐑒𐑩𐑯𐑛𐑧𐑥
condition|𐑒𐑩𐑯𐑛𐑦𐑖𐑩𐑯
confirm|𐑒𐑩𐑯𐑓𐑻𐑥
conflict|𐑒𐑩𐑯𐑓𐑤𐑦𐑒𐑑
conflict|𐑒𐑪𐑯𐑓𐑤𐑦𐑒𐑑
connect|𐑒𐑩𐑯𐑧𐑒𐑑
consider|𐑒𐑩𐑯𐑕𐑦𐑛𐑼
contact|𐑒𐑪𐑯𐑑𐑨𐑒𐑑
contain|𐑒𐑩𐑯𐑑𐑱𐑯
container|𐑒𐑩𐑯𐑑𐑱𐑯𐑼
continent|𐑒𐑪𐑯𐑑𐑦𐑯𐑩𐑯𐑑
continue|𐑒𐑩𐑯𐑑𐑦𐑯𐑿
control|𐑒𐑩𐑯𐑑𐑮𐑴𐑤
cooperate|𐑒𐑴𐑪𐑐𐑼𐑱𐑑
correct|𐑒𐑼𐑧𐑒𐑑
cotton|𐑒𐑪𐑑𐑩𐑯
count|𐑒𐑬𐑯𐑑
country|𐑒𐑳𐑯𐑑𐑮𐑦
court|𐑒𐑹𐑑
cover|𐑒𐑳𐑝𐑼
crash|𐑒𐑮𐑨𐑖
create|𐑒𐑮𐑦𐑱𐑑
creature|𐑒𐑮𐑰𐑗𐑼
credit|𐑒𐑮𐑧𐑛𐑦𐑑
crime|𐑒𐑮𐑲𐑥
criminal|𐑒𐑮𐑦𐑥𐑦𐑯𐑩𐑤
crisis|𐑒𐑮𐑲𐑕𐑦𐑕
criticize|𐑒𐑮𐑦𐑑𐑦𐑕𐑲𐑟
crops|𐑒𐑮𐑪𐑐𐑕
cross|𐑒𐑮𐑪𐑕
crowd|𐑒𐑮𐑬𐑛
crush|𐑒𐑮𐑳𐑖
culture|𐑒𐑳𐑤𐑗𐑼
curfew|𐑒𐑻𐑓𐑿
current|𐑒𐑳𐑮𐑩𐑯𐑑
custom|𐑒𐑳𐑕𐑑𐑩𐑥
customs|𐑒𐑳𐑕𐑑𐑩𐑥𐑟
damage|𐑛𐑨𐑥𐑦𐑡
dance|𐑛𐑨𐑯𐑕
dance|𐑛𐑭𐑯𐑕
danger|𐑛𐑱𐑯𐑡𐑼
daughter|𐑛𐑷𐑑𐑼
debate|𐑛𐑦𐑚𐑱𐑑
decide|𐑛𐑦𐑕𐑲𐑛
declare|𐑛𐑦𐑒𐑤𐑺
decrease|𐑛𐑦𐑒𐑮𐑰𐑕
decrease|𐑛𐑰𐑒𐑮𐑰𐑕
defeat|𐑛𐑦𐑓𐑰𐑑
defend|𐑛𐑦𐑓𐑧𐑯𐑛
deficit|𐑛𐑧𐑓𐑦𐑕𐑦𐑑
define|𐑛𐑦𐑓𐑲𐑯
degree|𐑛𐑦𐑜𐑮𐑰
delay|𐑛𐑦𐑤𐑱
delegate|𐑛𐑧𐑤𐑦𐑜𐑩𐑑
delegate|𐑛𐑧𐑤𐑦𐑜𐑱𐑑
demand|𐑛𐑦𐑥𐑨𐑯𐑛
demand|𐑛𐑦𐑥𐑭𐑯𐑛
democracy|𐑛𐑦𐑥𐑪𐑒𐑮𐑩𐑕𐑦
denounce|𐑛𐑦𐑯𐑬𐑯𐑕
depend|𐑛𐑦𐑐𐑧𐑯𐑛
deplore|𐑛𐑦𐑐𐑤𐑹
deploy|𐑛𐑦𐑐𐑤𐑶
describe|𐑛𐑦𐑕𐑒𐑮𐑲𐑚
desert|𐑛𐑦𐑟𐑻𐑑
desert|𐑛𐑧𐑟𐑼𐑑
design|𐑛𐑦𐑟𐑲𐑯
desire|𐑛𐑦𐑟𐑲𐑼
destroy|𐑛𐑦𐑕𐑑𐑮𐑶
detail|𐑛𐑰𐑑𐑱𐑤
detain|𐑛𐑦𐑑𐑱𐑯
develop|𐑛𐑦𐑝𐑧𐑤𐑩𐑐
device|𐑛𐑦𐑝𐑲𐑕
dictator|𐑛𐑦𐑒𐑑𐑱𐑑𐑼
different|𐑛𐑦𐑓𐑼𐑩𐑯𐑑
difficult|𐑛𐑦𐑓𐑦𐑒𐑩𐑤𐑑
dinner|𐑛𐑦𐑯𐑼
diplomat|𐑛𐑦𐑐𐑤𐑩𐑥𐑨𐑑
direct|𐑛𐑦𐑮𐑧𐑒𐑑
direction|𐑛𐑦𐑮𐑧𐑒𐑖𐑩𐑯
disappear|𐑛𐑦𐑕𐑩𐑐𐑽
disarm|𐑛𐑦𐑕𐑸𐑥
disaster|𐑛𐑦𐑟𐑨𐑕𐑑𐑼
disaster|𐑛𐑦𐑟𐑭𐑕𐑑𐑼
discover|𐑛𐑦𐑕𐑒𐑳𐑝𐑼
discuss|𐑛𐑦𐑕𐑒𐑳𐑕
disease|𐑛𐑦𐑟𐑰𐑟
dismiss|𐑛𐑦𐑕𐑥𐑦𐑕
dispute|𐑛𐑦𐑕𐑐𐑿𐑑
dissident|𐑛𐑦𐑕𐑦𐑛𐑩𐑯𐑑
distance|𐑛𐑦𐑕𐑑𐑩𐑯𐑕
divide|𐑛𐑦𐑝𐑲𐑛
doctor|𐑛𐑪𐑒𐑑𐑼
document|𐑛𐑪𐑒𐑘𐑩𐑥𐑧𐑯𐑑
document|𐑛𐑪𐑒𐑘𐑩𐑥𐑩𐑯𐑑
dollar|𐑛𐑪𐑤𐑼
donate|𐑛𐑴𐑯𐑱𐑑
double|𐑛𐑳𐑚𐑩𐑤
dream|𐑛𐑮𐑰𐑥
drink|𐑛𐑮𐑦𐑙𐑒
drive|𐑛𐑮𐑲𐑝
drown|𐑛𐑮𐑬𐑯
during|𐑛𐑘𐑫𐑼𐑦𐑙
early|𐑻𐑤𐑦
earth|𐑻𐑔
ecology|𐑰𐑒𐑪𐑤𐑩𐑡𐑦
economy|𐑦𐑒𐑪𐑯𐑩𐑥𐑦
education|𐑧𐑡𐑩𐑒𐑱𐑖𐑩𐑯
effect|𐑦𐑓𐑧𐑒𐑑
effort|𐑧𐑓𐑼𐑑
either|𐑲𐑞𐑼
elect|𐑦𐑤𐑧𐑒𐑑
embassy|𐑧𐑥𐑚𐑩𐑕𐑦
embryo|𐑧𐑥𐑚𐑮𐑦𐑴
emergency|𐑦𐑥𐑻𐑡𐑩𐑯𐑕𐑦
emotion|𐑦𐑥𐑴𐑖𐑩𐑯
employ|𐑦𐑥𐑐𐑤𐑶
empty|𐑧𐑥𐑐𐑑𐑦
enemy|𐑧𐑯𐑩𐑥𐑦
energy|𐑧𐑯𐑼𐑡𐑦
enforce|𐑦𐑯𐑓𐑹𐑕
engine|𐑧𐑯𐑡𐑦𐑯
engineer|𐑧𐑯𐑡𐑦𐑯𐑽
enjoy|𐑦𐑯𐑡𐑶
enough|𐑦𐑯𐑳𐑓
enter|𐑧𐑯𐑑𐑼
equal|𐑰𐑒𐑢𐑩𐑤
equipment|𐑦𐑒𐑢𐑦𐑐𐑥𐑩𐑯𐑑
escape|𐑦𐑕𐑒𐑱𐑐
establish|𐑦𐑕𐑑𐑨𐑚𐑤𐑦𐑖
estimate|𐑧𐑕𐑑𐑦𐑥𐑩𐑑
estimate|𐑧𐑕𐑑𐑦𐑥𐑱𐑑
ethnic|𐑧𐑔𐑯𐑦𐑒
evaporate|𐑦𐑝𐑨𐑐𐑼𐑱𐑑
event|𐑦𐑝𐑧𐑯𐑑
every|𐑧𐑝𐑮𐑦
evidence|𐑧𐑝𐑦𐑛𐑩𐑯𐑕
exact|𐑦𐑜𐑟𐑨𐑒𐑑
examine|𐑦𐑜𐑟𐑨𐑥𐑦𐑯
example|𐑦𐑜𐑟𐑨𐑥𐑐𐑩𐑤
example|𐑦𐑜𐑟𐑭𐑥𐑐𐑩𐑤
excellent|𐑧𐑒𐑕𐑩𐑤𐑩𐑯𐑑
except|𐑦𐑒𐑕𐑧𐑐𐑑
exchange|𐑦𐑒𐑕𐑗𐑱𐑯𐑡
excuse|𐑦𐑒𐑕𐑒𐑿𐑕
excuse|𐑦𐑒𐑕𐑒𐑿𐑟
execute|𐑧𐑒𐑕𐑦𐑒𐑿𐑑
exercise|𐑧𐑒𐑕𐑼𐑕𐑲𐑟
exile|𐑧𐑒𐑕𐑲𐑤
exist|𐑦𐑜𐑟𐑦𐑕𐑑
expand|𐑦𐑒𐑕𐑐𐑨𐑯𐑛
expect|𐑦𐑒𐑕𐑐𐑧𐑒𐑑
expel|𐑦𐑒𐑕𐑐𐑧𐑤
expert|𐑧𐑒𐑕𐑐𐑻𐑑
explain|𐑦𐑒𐑕𐑐𐑤𐑱𐑯
explode|𐑦𐑒𐑕𐑐𐑤𐑴𐑛
explore|𐑦𐑒𐑕𐑐𐑤𐑹
export|𐑦𐑒𐑕𐑐𐑹𐑑
export|𐑧𐑒𐑕𐑐𐑹𐑑
express|𐑦𐑒𐑕𐑐𐑮𐑧𐑕
extend|𐑦𐑒𐑕𐑑𐑧𐑯𐑛
extra|𐑧𐑒𐑕𐑑𐑮𐑩
extreme|𐑦𐑒𐑕𐑑𐑮𐑰𐑥
extremist|𐑦𐑒𐑕𐑑𐑮𐑰𐑥𐑦𐑕𐑑
factory|𐑓𐑨𐑒𐑑𐑼𐑦
false|𐑓𐑷𐑤𐑕
family|𐑓𐑨𐑥𐑦𐑤𐑦
famous|𐑓𐑱𐑥𐑩𐑕
father|𐑓𐑭𐑞𐑼
favorite|𐑓𐑱𐑝𐑼𐑦𐑑
federal|𐑓𐑧𐑛𐑼𐑩𐑤
female|𐑓𐑰𐑥𐑱𐑤
fence|𐑓𐑧𐑯𐑕
fertile|𐑓𐑻𐑑𐑲𐑤
field|𐑓𐑰𐑤𐑛
fierce|𐑓𐑽𐑕
fight|𐑓𐑲𐑑
final|𐑓𐑲𐑯𐑩𐑤
financial|𐑓𐑲𐑯𐑨𐑯𐑖𐑩𐑤
finish|𐑓𐑦𐑯𐑦𐑖
fireworks|𐑓𐑲𐑼𐑢𐑻𐑒𐑕
first|𐑓𐑻𐑕𐑑
float|𐑓𐑤𐑴𐑑
flood|𐑓𐑤𐑳𐑛
floor|𐑓𐑤𐑹
flower|𐑓𐑤𐑬𐑼
fluid|𐑓𐑤𐑵𐑦𐑛
follow|𐑓𐑪𐑤𐑴
force|𐑓𐑹𐑕
foreign|𐑓𐑪𐑮𐑦𐑯
forest|𐑓𐑪𐑮𐑦𐑕𐑑
forget|𐑓𐑼𐑜𐑧𐑑
forgive|𐑓𐑼𐑜𐑦𐑝
former|𐑓𐑹𐑥𐑼
forward|𐑓𐑹𐑢𐑼𐑛
freedom|𐑓𐑮𐑰𐑛𐑩𐑥
freeze|𐑓𐑮𐑰𐑟
fresh|𐑓𐑮𐑧𐑖
friend|𐑓𐑮𐑧𐑯𐑛
frighten|𐑓𐑮𐑲𐑑𐑩𐑯
front|𐑓𐑮𐑳𐑯𐑑
fruit|𐑓𐑮𐑵𐑑
funeral|𐑓𐑿𐑯𐑼𐑩𐑤
future|𐑓𐑿𐑗𐑼
gather|𐑜𐑨𐑞𐑼
general|𐑡𐑧𐑯𐑼𐑩𐑤
genocide|𐑡𐑧𐑯𐑩𐑕𐑲𐑛
gentle|𐑡𐑧𐑯𐑑𐑩𐑤
glass|𐑜𐑤𐑨𐑕
glass|𐑜𐑤𐑭𐑕
goods|𐑜𐑫𐑛𐑟
govern|𐑜𐑳𐑝𐑼𐑯
grain|𐑜𐑮𐑱𐑯
grass|𐑜𐑮𐑨𐑕
grass|𐑜𐑮𐑭𐑕
great|𐑜𐑮𐑱𐑑
green|𐑜𐑮𐑰𐑯
grind|𐑜𐑮𐑲𐑯𐑛
ground|𐑜𐑮𐑬𐑯𐑛
group|𐑜𐑮𐑵𐑐
guarantee|𐑜𐑨𐑮𐑩𐑯𐑑𐑰
guard|𐑜𐑸𐑛
guerrilla|𐑜𐑼𐑦𐑤𐑩
guide|𐑜𐑲𐑛
guilty|𐑜𐑦𐑤𐑑𐑦
happen|𐑣𐑨𐑐𐑩𐑯
happy|𐑣𐑨𐑐𐑦
harvest|𐑣𐑸𐑝𐑦𐑕𐑑
health|𐑣𐑧𐑤𐑔
heavy|𐑣𐑧𐑝𐑦
hijack|𐑣𐑲𐑡𐑨𐑒
history|𐑣𐑦𐑕𐑑𐑼𐑦
holiday|𐑣𐑪𐑤𐑦𐑛𐑱
honest|𐑪𐑯𐑩𐑕𐑑
honor|𐑪𐑯𐑼
horrible|𐑣𐑪𐑮𐑩𐑚𐑩𐑤
horse|𐑣𐑹𐑕
hospital|𐑣𐑪𐑕𐑐𐑦𐑑𐑩𐑤
hostage|𐑣𐑪𐑕𐑑𐑦𐑡
hostile|𐑣𐑪𐑕𐑑𐑲𐑤
hotel|𐑣𐑴𐑑𐑧𐑤
house|𐑣𐑬𐑕
house|𐑣𐑬𐑟
however|𐑣𐑬𐑧𐑝𐑼
human|𐑣𐑿𐑥𐑩𐑯
humor|𐑣𐑿𐑥𐑼
hunger|𐑣𐑳𐑙𐑜𐑼
hurry|𐑣𐑳𐑮𐑦
husband|𐑣𐑳𐑟𐑚𐑩𐑯𐑛
identify|𐑲𐑛𐑧𐑯𐑑𐑦𐑓𐑲
ignore|𐑦𐑜𐑯𐑹
illegal|𐑦𐑤𐑰𐑜𐑩𐑤
imagine|𐑦𐑥𐑨𐑡𐑦𐑯
immediate|𐑦𐑥𐑰𐑛𐑾𐑑
immigrant|𐑦𐑥𐑦𐑜𐑮𐑩𐑯𐑑
import|𐑦𐑥𐑐𐑹𐑑
important|𐑦𐑥𐑐𐑹𐑑𐑩𐑯𐑑
improve|𐑦𐑥𐑐𐑮𐑵𐑝
incident|𐑦𐑯𐑕𐑦𐑛𐑩𐑯𐑑
incite|𐑦𐑯𐑕𐑲𐑑
include|𐑦𐑯𐑒𐑤𐑵𐑛
increase|𐑦𐑯𐑒𐑮𐑰𐑕
industry|𐑦𐑯𐑛𐑩𐑕𐑑𐑮𐑦
infect|𐑦𐑯𐑓𐑧𐑒𐑑
inflation|𐑦𐑯𐑓𐑤𐑱𐑖𐑩𐑯
influence|𐑦𐑯𐑓𐑤𐑫𐑩𐑯𐑕
inform|𐑦𐑯𐑓𐑹𐑥
inject|𐑦𐑯𐑡𐑧𐑒𐑑
injure|𐑦𐑯𐑡𐑼
innocent|𐑦𐑯𐑩𐑕𐑩𐑯𐑑
insane|𐑦𐑯𐑕𐑱𐑯
insect|𐑦𐑯𐑕𐑧𐑒𐑑
inspect|𐑦𐑯𐑕𐑐𐑧𐑒𐑑
instead|𐑦𐑯𐑕𐑑𐑧𐑛
insult|𐑦𐑯𐑕𐑳𐑤𐑑
intense|𐑦𐑯𐑑𐑧𐑯𐑕
interest|𐑦𐑯𐑑𐑮𐑩𐑕𐑑
interfere|𐑦𐑯𐑑𐑼𐑓𐑽
intervene|𐑦𐑯𐑑𐑼𐑝𐑰𐑯
invade|𐑦𐑯𐑝𐑱𐑛
invent|𐑦𐑯𐑝𐑧𐑯𐑑
invest|𐑦𐑯𐑝𐑧𐑕𐑑
invite|𐑦𐑯𐑝𐑲𐑑
involve|𐑦𐑯𐑝𐑪𐑤𐑝
island|𐑲𐑤𐑩𐑯𐑛
issue|𐑦𐑖𐑵
jewel|𐑡𐑵𐑩𐑤
joint|𐑡𐑶𐑯𐑑
judge|𐑡𐑳𐑡
justice|𐑡𐑳𐑕𐑑𐑦𐑕
kidnap|𐑒𐑦𐑛𐑯𐑨𐑐
knife|𐑯𐑲𐑓
knowledge|𐑯𐑪𐑤𐑦𐑡
labor|𐑤𐑱𐑚𐑼
language|𐑤𐑨𐑙𐑜𐑢𐑦𐑡
large|𐑤𐑸𐑡
laugh|𐑤𐑨𐑓
laugh|𐑤𐑭𐑓
launch|𐑤𐑷𐑯𐑗
learn|𐑤𐑻𐑯
leave|𐑤𐑰𐑝
legal|𐑤𐑰𐑜𐑩𐑤
letter|𐑤𐑧𐑑𐑼
level|𐑤𐑧𐑝𐑩𐑤
liberal|𐑤𐑦𐑚𐑼𐑩𐑤
light|𐑤𐑲𐑑
lightning|𐑤𐑲𐑑𐑯𐑦𐑙
limit|𐑤𐑦𐑥𐑦𐑑
liquid|𐑤𐑦𐑒𐑢𐑦𐑛
listen|𐑤𐑦𐑕𐑩𐑯
little|𐑤𐑦𐑑𐑩𐑤
local|𐑤𐑴𐑒𐑩𐑤
lonely|𐑤𐑴𐑯𐑤𐑦
loyal|𐑤𐑶𐑩𐑤
machine|𐑥𐑩𐑖𐑰𐑯
magazine|𐑥𐑨𐑜𐑩𐑟𐑰𐑯
major|𐑥𐑱𐑡𐑼
majority|𐑥𐑩𐑡𐑪𐑮𐑦𐑑𐑦
march|𐑥𐑸𐑗
market|𐑥𐑸𐑒𐑩𐑑
marry|𐑥𐑨𐑮𐑦
material|𐑥𐑩𐑑𐑽𐑾𐑤
matter|𐑥𐑨𐑑𐑼
mayor|𐑥𐑺
measure|𐑥𐑧𐑠𐑼
media|𐑥𐑰𐑛𐑾
medicine|𐑥𐑧𐑛𐑦𐑕𐑩𐑯
member|𐑥𐑧𐑥𐑚𐑼
memorial|𐑥𐑩𐑥𐑹𐑾𐑤
memory|𐑥𐑧𐑥𐑼𐑦
mental|𐑥𐑧𐑯𐑑𐑩𐑤
message|𐑥𐑧𐑕𐑦𐑡
metal|𐑥𐑧𐑑𐑩𐑤
method|𐑥𐑧𐑔𐑩𐑛
middle|𐑥𐑦𐑛𐑩𐑤
militant|𐑥𐑦𐑤𐑦𐑑𐑩𐑯𐑑
military|𐑥𐑦𐑤𐑦𐑑𐑼𐑦
militia|𐑥𐑦𐑤𐑦𐑖𐑩
mineral|𐑥𐑦𐑯𐑼𐑩𐑤
minister|𐑥𐑦𐑯𐑦𐑕𐑑𐑼
minor|𐑥𐑲𐑯𐑼
minority|𐑥𐑲𐑯𐑪𐑮𐑦𐑑𐑦
minute|𐑥𐑦𐑯𐑦𐑑
minute|𐑥𐑲𐑯𐑿𐑑
missile|𐑥𐑦𐑕𐑲𐑤
missing|𐑥𐑦𐑕𐑦𐑙
mistake|𐑥𐑦𐑕𐑑𐑱𐑒
model|𐑥𐑪𐑛𐑩𐑤
moderate|𐑥𐑪𐑛𐑼𐑩𐑑
moderate|𐑥𐑪𐑛𐑼𐑱𐑑
modern|𐑥𐑪𐑛𐑼𐑯
money|𐑥𐑳𐑯𐑦
month|𐑥𐑳𐑯𐑔
moral|𐑥𐑪𐑮𐑩𐑤
morning|𐑥𐑹𐑯𐑦𐑙
mother|𐑥𐑳𐑞𐑼
motion|𐑥𐑴𐑖𐑩𐑯
mountain|𐑥𐑬𐑯𐑑𐑩𐑯
mourn|𐑥𐑹𐑯
movement|𐑥𐑵𐑝𐑥𐑩𐑯𐑑
movie|𐑥𐑵𐑝𐑦
murder|𐑥𐑻𐑛𐑼
music|𐑥𐑿𐑟𐑦𐑒
mystery|𐑥𐑦𐑕𐑑𐑼𐑦
narrow|𐑯𐑨𐑮𐑴
nation|𐑯𐑱𐑖𐑩𐑯
native|𐑯𐑱𐑑𐑦𐑝
natural|𐑯𐑨𐑗𐑼𐑩𐑤
nature|𐑯𐑱𐑗𐑼
necessary|𐑯𐑧𐑕𐑩𐑕𐑼𐑦
negotiate|𐑯𐑦𐑜𐑴𐑖𐑦𐑱𐑑
neighbor|𐑯𐑱𐑚𐑼
neither|𐑯𐑲𐑞𐑼
neutral|𐑯𐑿𐑑𐑮𐑩𐑤
never|𐑯𐑧𐑝𐑼
night|𐑯𐑲𐑑
noise|𐑯𐑶𐑟
nominate|𐑯𐑪𐑥𐑦𐑯𐑱𐑑
normal|𐑯𐑹𐑥𐑩𐑤
north|𐑯𐑹𐑔
nothing|𐑯𐑳𐑔𐑦𐑙
nowhere|𐑯𐑴𐑢𐑺
nuclear|𐑯𐑿𐑒𐑤𐑽
number|𐑯𐑳𐑥𐑚𐑼
object|𐑩𐑚𐑡𐑧𐑒𐑑
object|𐑪𐑚𐑡𐑧𐑒𐑑
observe|𐑩𐑚𐑟𐑻𐑝
occupy|𐑪𐑒𐑘𐑩𐑐𐑲
ocean|𐑴𐑖𐑩𐑯
offensive|𐑩𐑓𐑧𐑯𐑕𐑦𐑝
offer|𐑪𐑓𐑼
office|𐑪𐑓𐑦𐑕
officer|𐑪𐑓𐑦𐑕𐑼
official|𐑩𐑓𐑦𐑖𐑩𐑤
often|𐑪𐑓𐑩𐑯
operate|𐑪𐑐𐑼𐑱𐑑
opinion|𐑩𐑐𐑦𐑯𐑘𐑩𐑯
oppose|𐑩𐑐𐑴𐑟
opposite|𐑪𐑐𐑩𐑟𐑦𐑑
oppress|𐑩𐑐𐑮𐑧𐑕
orbit|𐑹𐑚𐑦𐑑
order|𐑹𐑛𐑼
organize|𐑹𐑜𐑩𐑯𐑲𐑟
other|𐑳𐑞𐑼
overthrow|𐑴𐑝𐑼𐑔𐑮𐑴
paint|𐑐𐑱𐑯𐑑
paper|𐑐𐑱𐑐𐑼
parachute|𐑐𐑨𐑮𐑩𐑖𐑵𐑑
parade|𐑐𐑼𐑱𐑛
pardon|𐑐𐑸𐑛𐑩𐑯
parent|𐑐𐑺𐑩𐑯𐑑
partner|𐑐𐑸𐑑𐑯𐑼
party|𐑐𐑸𐑑𐑦
passenger|𐑐𐑨𐑕𐑦𐑯𐑡𐑼
passport|𐑐𐑨𐑕𐑐𐑹𐑑
passport|𐑐𐑭𐑕𐑐𐑹𐑑
patient|𐑐𐑱𐑖𐑩𐑯𐑑
peace|𐑐𐑰𐑕
people|𐑐𐑰𐑐𐑩𐑤
percent|𐑐𐑼𐑕𐑧𐑯𐑑
perfect|𐑐𐑻𐑓𐑦𐑒𐑑
perfect|𐑐𐑼𐑓𐑧𐑒𐑑
perform|𐑐𐑼𐑓𐑹𐑥
period|𐑐𐑽𐑾𐑛
permanent|𐑐𐑻𐑥𐑩𐑯𐑩𐑯𐑑
permit|𐑐𐑻𐑥𐑦𐑑
permit|𐑐𐑼𐑥𐑦𐑑
person|𐑐𐑻𐑕𐑩𐑯
persuade|𐑐𐑼𐑕𐑢𐑱𐑛
physical|𐑓𐑦𐑟𐑦𐑒𐑩𐑤
physics|𐑓𐑦𐑟𐑦𐑒𐑕
picture|𐑐𐑦𐑒𐑗𐑼
piece|𐑐𐑰𐑕
pilot|𐑐𐑲𐑤𐑩𐑑
place|𐑐𐑤𐑱𐑕
planet|𐑐𐑤𐑨𐑯𐑩𐑑
plant|𐑐𐑤𐑨𐑯𐑑
plant|𐑐𐑤𐑭𐑯𐑑
plastic|𐑐𐑤𐑨𐑕𐑑𐑦𐑒
please|𐑐𐑤𐑰𐑟
plenty|𐑐𐑤𐑧𐑯𐑑𐑦
point|𐑐𐑶𐑯𐑑
poison|𐑐𐑶𐑟𐑩𐑯
police|𐑐𐑩𐑤𐑰𐑕
policy|𐑐𐑪𐑤𐑩𐑕𐑦
politics|𐑐𐑪𐑤𐑩𐑑𐑦𐑒𐑕
pollute|𐑐𐑩𐑤𐑵𐑑
popular|𐑐𐑪𐑐𐑘𐑩𐑤𐑼
position|𐑐𐑩𐑟𐑦𐑖𐑩𐑯
possess|𐑐𐑩𐑟𐑧𐑕
possible|𐑐𐑪𐑕𐑩𐑚𐑩𐑤
postpone|𐑐𐑴𐑕𐑑𐑐𐑴𐑯
poverty|𐑐𐑪𐑝𐑼𐑑𐑦
power|𐑐𐑬𐑼
praise|𐑐𐑮𐑱𐑟
predict|𐑐𐑮𐑦𐑛𐑦𐑒𐑑
pregnant|𐑐𐑮𐑧𐑜𐑯𐑩𐑯𐑑
present|𐑐𐑮𐑦𐑟𐑧𐑯𐑑
present|𐑐𐑮𐑧𐑟𐑩𐑯𐑑
president|𐑐𐑮𐑧𐑟𐑦𐑛𐑩𐑯𐑑
press|𐑐𐑮𐑧𐑕
pressure|𐑐𐑮𐑧𐑖𐑼
prevent|𐑐𐑮𐑦𐑝𐑧𐑯𐑑
price|𐑐𐑮𐑲𐑕
prison|𐑐𐑮𐑦𐑟𐑩𐑯
private|𐑐𐑮𐑲𐑝𐑩𐑑
prize|𐑐𐑮𐑲𐑟
probably|𐑐𐑮𐑪𐑚𐑩𐑚𐑤𐑦
problem|𐑐𐑮𐑪𐑚𐑤𐑩𐑥
process|𐑐𐑮𐑩𐑕𐑧𐑕
process|𐑐𐑮𐑴𐑕𐑧𐑕
produce|𐑐𐑮𐑩𐑛𐑿𐑕
produce|𐑐𐑮𐑪𐑛𐑿𐑕
professor|𐑐𐑮𐑩𐑓𐑧𐑕𐑼
profit|𐑐𐑮𐑪𐑓𐑦𐑑
program|𐑐𐑮𐑴𐑜𐑮𐑨𐑥
progress|𐑐𐑮𐑩𐑜𐑮𐑧𐑕
progress|𐑐𐑮𐑴𐑜𐑮𐑧𐑕
project|𐑐𐑮𐑩𐑡𐑧𐑒𐑑
project|𐑐𐑮𐑪𐑡𐑧𐑒𐑑
promise|𐑐𐑮𐑪𐑥𐑦𐑕
property|𐑐𐑮𐑪𐑐𐑼𐑑𐑦
propose|𐑐𐑮𐑩𐑐𐑴𐑟
protect|𐑐𐑮𐑩𐑑𐑧𐑒𐑑
protest|𐑐𐑮𐑩𐑑𐑧𐑕𐑑
protest|𐑐𐑮𐑴𐑑𐑧𐑕𐑑
prove|𐑐𐑮𐑵𐑝
provide|𐑐𐑮𐑩𐑝𐑲𐑛
public|𐑐𐑳𐑚𐑤𐑦𐑒
publish|𐑐𐑳𐑚𐑤𐑦𐑖
punish|𐑐𐑳𐑯𐑦𐑖
purchase|𐑐𐑻𐑗𐑩𐑕
purpose|𐑐𐑻𐑐𐑩𐑕
quality|𐑒𐑢𐑪𐑤𐑦𐑑𐑦
question|𐑒𐑢𐑧𐑕𐑗𐑩𐑯
quick|𐑒𐑢𐑦𐑒
quiet|𐑒𐑢𐑲𐑩𐑑
radar|𐑮𐑱𐑛𐑸
radiation|𐑮𐑱𐑛𐑦𐑱𐑖𐑩𐑯
radio|𐑮𐑱𐑛𐑦𐑴
railroad|𐑮𐑱𐑤𐑮𐑴𐑛
raise|𐑮𐑱𐑟
reach|𐑮𐑰𐑗
react|𐑮𐑦𐑨𐑒𐑑
ready|𐑮𐑧𐑛𐑦
realistic|𐑮𐑾𐑤𐑦𐑕𐑑𐑦𐑒
reason|𐑮𐑰𐑟𐑩𐑯
rebel|𐑮𐑦𐑚𐑧𐑤
rebel|𐑮𐑧𐑚𐑩𐑤
receive|𐑮𐑦𐑕𐑰𐑝
recent|𐑮𐑰𐑕𐑩𐑯𐑑
recession|𐑮𐑦𐑕𐑧𐑖𐑩𐑯
recognize|𐑮𐑧𐑒𐑩𐑜𐑯𐑲𐑟
record|𐑮𐑦𐑒𐑹𐑛
record|𐑮𐑧𐑒𐑹𐑛
recover|𐑮𐑦𐑒𐑳𐑝𐑼
reduce|𐑮𐑦𐑛𐑿𐑕
reform|𐑮𐑦𐑓𐑹𐑥
refugee|𐑮𐑧𐑓𐑘𐑫𐑡𐑰
refuse|𐑮𐑦𐑓𐑿𐑟
refuse|𐑮𐑧𐑓𐑿𐑕
register|𐑮𐑧𐑡𐑦𐑕𐑑𐑼
regret|𐑮𐑦𐑜𐑮𐑧𐑑
reject|𐑮𐑦𐑡𐑧𐑒𐑑
reject|𐑮𐑰𐑡𐑧𐑒𐑑
relations|𐑮𐑦𐑤𐑱𐑖𐑩𐑯𐑟
release|𐑮𐑦𐑤𐑰𐑕
religion|𐑮𐑦𐑤𐑦𐑡𐑩𐑯
remain|𐑮𐑦𐑥𐑱𐑯
remains|𐑮𐑦𐑥𐑱𐑯𐑟
remember|𐑮𐑦𐑥𐑧𐑥𐑚𐑼
remove|𐑮𐑦𐑥𐑵𐑝
repair|𐑮𐑦𐑐𐑺
repeat|𐑮𐑦𐑐𐑰𐑑
report|𐑮𐑦𐑐𐑹𐑑
represent|𐑮𐑧𐑐𐑮𐑦𐑟𐑧𐑯𐑑
represent|𐑮𐑰𐑐𐑮𐑦𐑟𐑧𐑯𐑑
repress|𐑮𐑦𐑐𐑮𐑧𐑕
request|𐑮𐑦𐑒𐑢𐑧𐑕𐑑
require|𐑮𐑦𐑒𐑢𐑲𐑼
rescue|𐑮𐑧𐑕𐑒𐑿
research|𐑮𐑦𐑕𐑻𐑗
resign|𐑮𐑦𐑟𐑲𐑯
resist|𐑮𐑦𐑟𐑦𐑕𐑑
resource|𐑮𐑦𐑟𐑹𐑕
respect|𐑮𐑦𐑕𐑐𐑧𐑒𐑑
restrain|𐑮𐑦𐑕𐑑𐑮𐑱𐑯
restrict|𐑮𐑦𐑕𐑑𐑮𐑦𐑒𐑑
result|𐑮𐑦𐑟𐑳𐑤𐑑
retire|𐑮𐑦𐑑𐑲𐑼
return|𐑮𐑦𐑑𐑻𐑯
revolt|𐑮𐑦𐑝𐑴𐑤𐑑
right|𐑮𐑲𐑑
rights|𐑮𐑲𐑑𐑕
river|𐑮𐑦𐑝𐑼
rocket|𐑮𐑪𐑒𐑩𐑑
rough|𐑮𐑳𐑓
round|𐑮𐑬𐑯𐑛
rubber|𐑮𐑳𐑚𐑼
rural|𐑮𐑫𐑼𐑩𐑤
sabotage|𐑕𐑨𐑚𐑩𐑑𐑭𐑠
sacrifice|𐑕𐑨𐑒𐑮𐑦𐑓𐑲𐑕
sailor|𐑕𐑱𐑤𐑼
satellite|𐑕𐑨𐑑𐑩𐑤𐑲𐑑
satisfy|𐑕𐑨𐑑𐑦𐑕𐑓𐑲
school|𐑕𐑒𐑵𐑤
science|𐑕𐑲𐑩𐑯𐑕
search|𐑕𐑻𐑗
season|𐑕𐑰𐑟𐑩𐑯
second|𐑕𐑦𐑒𐑪𐑯𐑛
second|𐑕𐑧𐑒𐑩𐑯𐑛
secret|𐑕𐑰𐑒𐑮𐑩𐑑
security|𐑕𐑦𐑒𐑘𐑫𐑼𐑦𐑑𐑦
seeking|𐑕𐑰𐑒𐑦𐑙
seize|𐑕𐑰𐑟
sense|𐑕𐑧𐑯𐑕
sentence|𐑕𐑧𐑯𐑑𐑩𐑯𐑕
separate|𐑕𐑧𐑐𐑼𐑩𐑑
separate|𐑕𐑧𐑐𐑼𐑱𐑑
series|𐑕𐑽𐑰𐑟
serious|𐑕𐑽𐑾𐑕
serve|𐑕𐑻𐑝
service|𐑕𐑻𐑝𐑦𐑕
settle|𐑕𐑧𐑑𐑩𐑤
several|𐑕𐑧𐑝𐑼𐑩𐑤
severe|𐑕𐑦𐑝𐑽
shake|𐑖𐑱𐑒
shape|𐑖𐑱𐑐
share|𐑖𐑺
sharp|𐑖𐑸𐑐
sheep|𐑖𐑰𐑐
shell|𐑖𐑧𐑤
shelter|𐑖𐑧𐑤𐑑𐑼
shine|𐑖𐑲𐑯
shock|𐑖𐑪𐑒
shoot|𐑖𐑵𐑑
short|𐑖𐑹𐑑
should|𐑖𐑫𐑛
shout|𐑖𐑬𐑑
shrink|𐑖𐑮𐑦𐑙𐑒
sickness|𐑕𐑦𐑒𐑯𐑩𐑕
signal|𐑕𐑦𐑜𐑯𐑩𐑤
silence|𐑕𐑲𐑤𐑩𐑯𐑕
silver|𐑕𐑦𐑤𐑝𐑼
similar|𐑕𐑦𐑥𐑦𐑤𐑼
simple|𐑕𐑦𐑥𐑐𐑩𐑤
since|𐑕𐑦𐑯𐑕
single|𐑕𐑦𐑙𐑜𐑩𐑤
sister|𐑕𐑦𐑕𐑑𐑼
situation|𐑕𐑦𐑗𐑫𐑱𐑖𐑩𐑯
skeleton|𐑕𐑒𐑧𐑤𐑦𐑑𐑩𐑯
skill|𐑕𐑒𐑦𐑤
slave|𐑕𐑤𐑱𐑝
sleep|𐑕𐑤𐑰𐑐
slide|𐑕𐑤𐑲𐑛
small|𐑕𐑥𐑷𐑤
smash|𐑕𐑥𐑨𐑖
smell|𐑕𐑥𐑧𐑤
smoke|𐑕𐑥𐑴𐑒
smooth|𐑕𐑥𐑵𐑞
social|𐑕𐑴𐑖𐑩𐑤
soldier|𐑕𐑴𐑤𐑡𐑼
solid|𐑕𐑪𐑤𐑦𐑛
solve|𐑕𐑪𐑤𐑝
sound|𐑕𐑬𐑯𐑛
south|𐑕𐑬𐑔
space|𐑕𐑐𐑱𐑕
speak|𐑕𐑐𐑰𐑒
special|𐑕𐑐𐑧𐑖𐑩𐑤
speech|𐑕𐑐𐑰𐑗
speed|𐑕𐑐𐑰𐑛
spend|𐑕𐑐𐑧𐑯𐑛
spill|𐑕𐑐𐑦𐑤
spirit|𐑕𐑐𐑦𐑮𐑦𐑑
split|𐑕𐑐𐑤𐑦𐑑
sport|𐑕𐑐𐑹𐑑
spread|𐑕𐑐𐑮𐑧𐑛
spring|𐑕𐑐𐑮𐑦𐑙
square|𐑕𐑒𐑢𐑺
stand|𐑕𐑑𐑨𐑯𐑛
start|𐑕𐑑𐑸𐑑
starve|𐑕𐑑𐑸𐑝
state|𐑕𐑑𐑱𐑑
station|𐑕𐑑𐑱𐑖𐑩𐑯
statue|𐑕𐑑𐑨𐑗𐑵
steal|𐑕𐑑𐑰𐑤
steam|𐑕𐑑𐑰𐑥
steel|𐑕𐑑𐑰𐑤
stick|𐑕𐑑𐑦𐑒
still|𐑕𐑑𐑦𐑤
stone|𐑕𐑑𐑴𐑯
store|𐑕𐑑𐑹
storm|𐑕𐑑𐑹𐑥
story|𐑕𐑑𐑹𐑦
stove|𐑕𐑑𐑴𐑝
straight|𐑕𐑑𐑮𐑱𐑑
strange|𐑕𐑑𐑮𐑱𐑯𐑡
street|𐑕𐑑𐑮𐑰𐑑
stretch|𐑕𐑑𐑮𐑧𐑗
strike|𐑕𐑑𐑮𐑲𐑒
strong|𐑕𐑑𐑮𐑪𐑙
structure|𐑕𐑑𐑮𐑳𐑒𐑗𐑼
struggle|𐑕𐑑𐑮𐑳𐑜𐑩𐑤
study|𐑕𐑑𐑳𐑛𐑦
stupid|𐑕𐑑𐑿𐑐𐑦𐑛
subject|𐑕𐑩𐑚𐑡𐑧𐑒𐑑
subject|𐑕𐑳𐑚𐑡𐑧𐑒𐑑
submarine|𐑕𐑳𐑚𐑥𐑼𐑰𐑯
substance|𐑕𐑳𐑚𐑕𐑑𐑩𐑯𐑕
succeed|𐑕𐑩𐑒𐑕𐑰𐑛
sudden|𐑕𐑳𐑛𐑩𐑯
suffer|𐑕𐑳𐑓𐑼
sugar|𐑖𐑫𐑜𐑼
suggest|𐑕𐑩𐑡𐑧𐑕𐑑
suicide|𐑕𐑵𐑦𐑕𐑲𐑛
summer|𐑕𐑳𐑥𐑼
supervise|𐑕𐑵𐑐𐑼𐑝𐑲𐑟
supply|𐑕𐑩𐑐𐑤𐑲
support|𐑕𐑩𐑐𐑹𐑑
suppose|𐑕𐑩𐑐𐑴𐑟
suppress|𐑕𐑩𐑐𐑮𐑧𐑕
surface|𐑕𐑻𐑓𐑦𐑕
surplus|𐑕𐑻𐑐𐑤𐑩𐑕
surprise|𐑕𐑼𐑐𐑮𐑲𐑟
surrender|𐑕𐑼𐑧𐑯𐑛𐑼
surround|𐑕𐑼𐑬𐑯𐑛
survive|𐑕𐑼𐑝𐑲𐑝
suspect|𐑕𐑩𐑕𐑐𐑧𐑒𐑑
suspect|𐑕𐑳𐑕𐑐𐑧𐑒𐑑
suspend|𐑕𐑩𐑕𐑐𐑧𐑯𐑛
swallow|𐑕𐑢𐑪𐑤𐑴
swear|𐑕𐑢𐑺
sweet|𐑕𐑢𐑰𐑑
sympathy|𐑕𐑦𐑥𐑐𐑩𐑔𐑦
system|𐑕𐑦𐑕𐑑𐑩𐑥
target|𐑑𐑸𐑜𐑩𐑑
taste|𐑑𐑱𐑕𐑑
teach|𐑑𐑰𐑗
technical|𐑑𐑧𐑒𐑯𐑦𐑒𐑩𐑤
telephone|𐑑𐑧𐑤𐑦𐑓𐑴𐑯
telescope|𐑑𐑧𐑤𐑦𐑕𐑒𐑴𐑐
temporary|𐑑𐑧𐑥𐑐𐑼𐑼𐑦
tense|𐑑𐑧𐑯𐑕
terrible|𐑑𐑧𐑮𐑩𐑚𐑩𐑤
territory|𐑑𐑧𐑮𐑦𐑑𐑼𐑦
terror|𐑑𐑧𐑮𐑼
terrorist|𐑑𐑧𐑮𐑼𐑦𐑕𐑑
thank|𐑔𐑨𐑙𐑒
theater|𐑔𐑾𐑑𐑼
theory|𐑔𐑽𐑦
there|𐑞𐑺
these|𐑞𐑰𐑟
thick|𐑔𐑦𐑒
thing|𐑔𐑦𐑙
think|𐑔𐑦𐑙𐑒
third|𐑔𐑻𐑛
threaten|𐑔𐑮𐑧𐑑𐑩𐑯
through|𐑔𐑮𐑵
throw|𐑔𐑮𐑴
tired|𐑑𐑲𐑼𐑛
today|𐑑𐑩𐑛𐑱
together|𐑑𐑩𐑜𐑧𐑞𐑼
tomorrow|𐑑𐑩𐑥𐑪𐑮𐑴
tonight|𐑑𐑩𐑯𐑲𐑑
torture|𐑑𐑹𐑗𐑼
total|𐑑𐑴𐑑𐑩𐑤
touch|𐑑𐑳𐑗
toward|𐑑𐑩𐑢𐑹𐑛
trade|𐑑𐑮𐑱𐑛
tradition|𐑑𐑮𐑩𐑛𐑦𐑖𐑩𐑯
traffic|𐑑𐑮𐑨𐑓𐑦𐑒
tragic|𐑑𐑮𐑨𐑡𐑦𐑒
train|𐑑𐑮𐑱𐑯
transport|𐑑𐑮𐑨𐑯𐑕𐑐𐑹𐑑
travel|𐑑𐑮𐑨𐑝𐑩𐑤
treason|𐑑𐑮𐑰𐑟𐑩𐑯
treasure|𐑑𐑮𐑧𐑠𐑼
treat|𐑑𐑮𐑰𐑑
treatment|𐑑𐑮𐑰𐑑𐑥𐑩𐑯𐑑
treaty|𐑑𐑮𐑰𐑑𐑦
trial|𐑑𐑮𐑲𐑩𐑤
tribe|𐑑𐑮𐑲𐑚
trick|𐑑𐑮𐑦𐑒
troops|𐑑𐑮𐑵𐑐𐑕
trouble|𐑑𐑮𐑳𐑚𐑩𐑤
truce|𐑑𐑮𐑵𐑕
truck|𐑑𐑮𐑳𐑒
trust|𐑑𐑮𐑳𐑕𐑑
under|𐑳𐑯𐑛𐑼
unite|𐑿𐑯𐑲𐑑
universe|𐑿𐑯𐑦𐑝𐑻𐑕
unless|𐑩𐑯𐑤𐑧𐑕
until|𐑩𐑯𐑑𐑦𐑤
urgent|𐑻𐑡𐑩𐑯𐑑
usual|𐑿𐑠𐑫𐑩𐑤
vacation|𐑝𐑱𐑒𐑱𐑖𐑩𐑯
vaccine|𐑝𐑨𐑒𐑕𐑰𐑯
valley|𐑝𐑨𐑤𐑦
value|𐑝𐑨𐑤𐑿
vegetable|𐑝𐑧𐑡𐑑𐑩𐑚𐑩𐑤
vehicle|𐑝𐑰𐑦𐑒𐑩𐑤
version|𐑝𐑻𐑠𐑩𐑯
victim|𐑝𐑦𐑒𐑑𐑦𐑥
victory|𐑝𐑦𐑒𐑑𐑼𐑦
video|𐑝𐑦𐑛𐑦𐑴
village|𐑝𐑦𐑤𐑦𐑡
violate|𐑝𐑲𐑩𐑤𐑱𐑑
violence|𐑝𐑲𐑩𐑤𐑩𐑯𐑕
visit|𐑝𐑦𐑟𐑦𐑑
voice|𐑝𐑶𐑕
volcano|𐑝𐑪𐑤𐑒𐑱𐑯𐑴
volunteer|𐑝𐑪𐑤𐑩𐑯𐑑𐑽
wages|𐑢𐑱𐑡𐑩𐑟
waste|𐑢𐑱𐑕𐑑
watch|𐑢𐑪𐑗
water|𐑢𐑷𐑑𐑼
wealth|𐑢𐑧𐑤𐑔
weapon|𐑢𐑧𐑐𐑩𐑯
weather|𐑢𐑧𐑞𐑼
weigh|𐑢𐑱
welcome|𐑢𐑧𐑤𐑒𐑩𐑥
wheat|𐑢𐑰𐑑
wheel|𐑢𐑰𐑤
where|𐑢𐑺
whether|𐑢𐑧𐑞𐑼
which|𐑢𐑦𐑗
while|𐑢𐑲𐑤
white|𐑢𐑲𐑑
whole|𐑣𐑴𐑤
willing|𐑢𐑦𐑤𐑦𐑙
window|𐑢𐑦𐑯𐑛𐑴
winter|𐑢𐑦𐑯𐑑𐑼
withdraw|𐑢𐑦𐑞𐑛𐑮𐑷
without|𐑢𐑦𐑞𐑬𐑑
witness|𐑢𐑦𐑑𐑯𐑩𐑕
woman|𐑢𐑫𐑥𐑩𐑯
wonder|𐑢𐑳𐑯𐑛𐑼
wonderful|𐑢𐑳𐑯𐑛𐑼𐑓𐑩𐑤
world|𐑢𐑻𐑤𐑛
worry|𐑢𐑳𐑮𐑦
worse|𐑢𐑻𐑕
worth|𐑢𐑻𐑔
wound|𐑢𐑬𐑯𐑛
wound|𐑢𐑵𐑯𐑛
wreck|𐑮𐑧𐑒
wreckage|𐑮𐑧𐑒𐑦𐑡
write|𐑮𐑲𐑑
wrong|𐑮𐑪𐑙
yellow|𐑘𐑧𐑤𐑴
yesterday|𐑘𐑧𐑕𐑑𐑼𐑛𐑱
young|𐑘𐑳𐑙

"""

# Split the input string by new lines and strip any extra whitespace
input_list = [record.strip() for record in input_string.strip().split('\n') if record.strip()]

# Initialize an empty list to hold the dictionaries
result = []

# Iterate over each record in the input list
for record in input_list:
    # Split the record by '|'
    elements = record.split('|')
    
    # Check if there are exactly two elements to avoid index errors
    if len(elements) == 2:
        # Create a dictionary with specified keys
        record_dict = {
            "english": elements[0],  # First part as "english"
            "shavian": elements[1]    # Second part as "shavian"
        }
        # Append the dictionary to the result list
        result.append(record_dict)
    else:
        print(f"Skipping invalid record: {record}")

# Print each dictionary on a new line with a comma at the end of each line except the last one
for i, item in enumerate(result):
    print(item, end=",\n" if i < len(result) - 1 else "\n")
