from pupil import Pupil as P
from group import Group as G
from subject import Subject as S
from timetable import Timetable as T
from class_ import Class


vasiliyBobrov = P(181458569, "Василий Бобров")
daniilMerinov = P(414200720, "Данил Меринов")
igorTuchin = P(217861131, "Игорь Тучин")
daniilBeliy = P(209403238, "Даниил Белый")
maximKarbyshev = P(155208579, "Макс Карбышев")
veronikaAvdeeva = P(243713812, "Вероника Авдеева")
antonOklei = P(135273078, "Антон Оклей")
ivanKuzmin = P(263338947, "Иван Кузьмин")
alexandrNikitin = P(68997073, "Александр Никитин")
annaKudravceva = P(194701120, "Анна Кудрявцева")
levYavna = P(34603639, "Лев Явна")
artemZubko = P(170684515, "Артём Зубко")
olegPotehin = P(209368755, "Олег Потехин")
sashaIlushenko = P(174515051, "Саша Илющенко")
alyaVlasenkova = P(192201480, "Аля Власенкова")
semenPanov = P(217619441, "Семен Панов")
evgeniyZimin = P(165027741, "Евгений Зимин")
egorShkolnikov = P(63875925, "Егор Школьников")
temaFedorov = P(222017849, "Тёма Фёдоров")
fedorKorolkov = P(174066292, "Фёдор Корольков")
dimaParfenov = P(173130572, "Дима Парфёнов")
fomaShipilov = P(249784999, "Фома Шипилов")
katyaShamarina = P(244623917, "Катя Шамарина")
egorMazin = P(321223794, "Егор Мазин")
ilyaRojkov = P(241922285, "Илья Рожков")
sergeiKalabashkin = P(166676709, "Сергей Калабашкин")

pupils = [vasiliyBobrov, daniilMerinov, igorTuchin, daniilBeliy, maximKarbyshev, veronikaAvdeeva, antonOklei, ivanKuzmin, alexandrNikitin, 
		annaKudravceva, levYavna, artemZubko, olegPotehin, sashaIlushenko, alyaVlasenkova, semenPanov, evgeniyZimin, egorShkolnikov, temaFedorov,
		fedorKorolkov, dimaParfenov, fomaShipilov, katyaShamarina, egorMazin, ilyaRojkov, sergeiKalabashkin]



ptGroup1 = G("(I) Группа Ники", [veronikaAvdeeva, alyaVlasenkova, sergeiKalabashkin, fedorKorolkov, alexandrNikitin, dimaParfenov, olegPotehin, ilyaRojkov, fomaShipilov])
ptGroup2 = G("(II) Группа Васи", [vasiliyBobrov, daniilMerinov, igorTuchin, antonOklei, sashaIlushenko, evgeniyZimin, temaFedorov, egorShkolnikov])
ptGroup3 = G("(III) Группа Дани", [daniilBeliy, maximKarbyshev, artemZubko, ivanKuzmin, annaKudravceva, egorMazin, semenPanov, katyaShamarina, levYavna])
engGroupTU = G("Группа Татьяны Юрьевны", [vasiliyBobrov, daniilBeliy, igorTuchin, daniilMerinov, maximKarbyshev, veronikaAvdeeva, antonOklei, ivanKuzmin, sashaIlushenko, alyaVlasenkova, semenPanov, temaFedorov, ilyaRojkov])
engGroupMN = G("Группа Марины Николаевны", [egorShkolnikov, levYavna, alexandrNikitin, katyaShamarina, evgeniyZimin, sergeiKalabashkin, annaKudravceva, egorMazin, fedorKorolkov, artemZubko, dimaParfenov, olegPotehin, fomaShipilov])
general = G("Весь класс", pupils)


physics = S("Физика", ['физику', 'физике'], [general])
algebra = S("Алгебра", ["алга", "алгу", "алгебру", 'алгебре'], [ptGroup1, ptGroup2, ptGroup3])
geometry = S("Геометрия", ["геомка", "геома", "геомку", "геому", "геометрию", 'геометрии', 'геоме', 'геомке'], [general])
literature = S("Литература", ["литра", "лит-ра", "литру", "лит-ру", "литературу", 'литературе', 'литре', 'лит-ре'], [general])
russian = S("Русский язык", ["русский", "русич", "русск яз", "русск. яз.", 'русскому', 'русичу', 'русскому языку'], [general])
english = S("Английский язык", ["английский", "англ яз", "англ. яз.", "инглиш", 'инглишу', 'английскому', 'английскому языку'], [engGroupTU, engGroupMN])
physCulture = S("Физкультура", ["физра", "физ-ра", "физру", "физ-ру", "физкультуру", 'физкультуре', 'физре', 'физ-ре'], [general])
biology = S("Биология", ["биологию", 'биологии'], [general])
history = S("История", ["историю", 'истории'], [general])
obj = S("Обж", None, [general])
astronomy = S("Астрономия", ["астрономию", 'астрономии'], [general])
astrophysics = S("Астрофизика", ["астрофизику", 'астрофизике'], [general])
zftsha = S("ЗФТШ", None, [general])
informatics = S("Информатика", ["инфа", "программирование", "информатику", "инфу", 'информатике', 'инфе', 'программированию'], [general])
chemistry = S("Химия", ["химию", 'химии'], [general])
geography = S("География", ["географию", "гео", 'географии'], [general])
mathAnalysis = S("Мат. анализ", ["математический анализ", "матан", 'мат. анализу', 'математическому анализу', 'матану', 'мат анализ', 'мат анализу'], [general])
expPhysics = S("Экспериментальная физика", ["эксп. физика", "эксп физика", "экспериментальную физику", "эксп. физику", "эксп физику", 
				'экспериментальной физике', 'эксп физике', 'эксп. физике'], [general])
socialStudies = S("Обществознание", ["общага", "общество", "общагу", 'общаге', 'обществознанию', 'обществу'], [general])
egeRussian = S("Русский ЕГЭ", ["русич егэ", "доп. русский", "доп русский", "дополнительный русский", "егэ русский", 
				"русскому егэ", "русичу егэ", "доп. русскому", "доп русскому", "дополнительному русскому", "егэ русскому"], [general])

subjects = [physics, algebra, geometry, literature, russian, english, physCulture, biology, history, obj, astronomy, astrophysics, zftsha, informatics,
			chemistry, geography, mathAnalysis, expPhysics, socialStudies, egeRussian]


monday1 = (1, [english, geometry, geometry, algebra, algebra, physics, physics])
monday2 = (1, [english, algebra, algebra, physics, physics, geometry, geometry])
monday3 = (1, [english, physics, physics, geometry, geometry, algebra, algebra])
tuesday = (2, [physCulture, literature, english, russian, biology, history, biology])
wednesday1 = (3, [history, obj, english, astronomy, algebra, astrophysics, geometry])
wednesday2 = (3, [history, obj, english, astronomy, geometry, algebra, astrophysics])
wednesday3 = (3, [history, obj, english, astronomy, astrophysics, geometry, algebra])
thursday1 = (4, [informatics, informatics, physics, physics, zftsha, zftsha])
thursday2 = (4, [physics, physics, zftsha, zftsha, informatics, informatics])
thursday3 = (4, [zftsha, zftsha, informatics, informatics, physics, physics])
friday1 = (5, [literature, physCulture, literature, chemistry, chemistry, geography])
friday2 = (5, [literature, physCulture, literature, chemistry, chemistry, socialStudies])
saturday1 = (6, [expPhysics, expPhysics, physics, physics, mathAnalysis, mathAnalysis])
saturday2 = (6, [mathAnalysis, mathAnalysis, expPhysics, expPhysics, physics, physics])
saturday3 = (6, [physics, physics, mathAnalysis, mathAnalysis, expPhysics, expPhysics])



timetable1 = T()
timetable1.setPupils([sergeiKalabashkin, fedorKorolkov, alexandrNikitin, dimaParfenov, olegPotehin, fomaShipilov])
timetable1.setSubjects(*monday1)
timetable1.setSubjects(*tuesday)
timetable1.setSubjects(*wednesday1)
timetable1.setSubjects(*thursday1)
timetable1.setSubjects(*friday1)
timetable1.setSubjects(*saturday1)

timetable1_2 = timetable1.copy()
timetable1_2.setPupils([veronikaAvdeeva, alyaVlasenkova, ilyaRojkov])
timetable1_2.setSubjects(*friday2)

timetable2 = T()
timetable2.setPupils([vasiliyBobrov, daniilMerinov, igorTuchin, antonOklei, evgeniyZimin, egorShkolnikov])
timetable2.setSubjects(*monday2)
timetable2.setSubjects(*tuesday)
timetable2.setSubjects(*wednesday2)
timetable2.setSubjects(*thursday2)
timetable2.setSubjects(*friday1)
timetable2.setSubjects(*saturday2)

timetable2_2 = timetable1.copy()
timetable2_2.setPupils([sashaIlushenko, temaFedorov])
timetable2_2.setSubjects(*friday2)

timetable3 = T()
timetable3.setPupils([daniilBeliy, maximKarbyshev, artemZubko, ivanKuzmin, annaKudravceva, egorMazin, katyaShamarina, levYavna])
timetable3.setSubjects(*monday3)
timetable3.setSubjects(*tuesday)
timetable3.setSubjects(*wednesday3)
timetable3.setSubjects(*thursday3)
timetable3.setSubjects(*friday1)
timetable3.setSubjects(*saturday3)

timetable3_2 = timetable1.copy()
timetable3_2.setPupils([semenPanov])
timetable3_2.setSubjects(*friday2)






class_ = Class('kurchat10z', pupils, subjects)

