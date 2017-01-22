import urllib2
import sys
from BeautifulSoup import BeautifulSoup

sys.stdout = open('public_scrape.txt', 'w')

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

url = " # Enter url of the public profile "
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl)

profile = soup.findChildren('div', attrs={'id': 'profile'})
profile_overview = profile[0].findChildren('div', attrs={'class': 'profile-overview'})
profile_content = soup.findChildren('div', attrs={'class': 'profile-overview-content'})
name = profile_content[0].find('h1', attrs={'class': 'fn'}).text
print 'Name: ' + str(name)
headline_title = profile_content[0].find('p', attrs={'class': 'headline title'}).text
print 'Info: ' + str(headline_title)
extra_info = profile_content[0].findChildren('table', attrs={'class': 'extra-info'})

if (profile_content[0].findChildren('dl', attrs={'id': 'demographics'})):
    demographics = profile_content[0].findChildren('dl', attrs={'id': 'demographics'})
    get_tags_demographics_dt = demographics[0].findAll('dt')
    for each in get_tags_demographics_dt:
        print each.contents[0] + ': ' + str(each.findNext('dd').text)

    print ''
    print '-----------------------------------------------------------------'
    print ''

if (profile_content[0].find('table', attrs={'class': 'extra-info'})):
    current_info = extra_info[0].findChildren('tr', attrs={'data-section': 'currentPositionsDetails'})
    current_info_all = current_info[0].findChildren('ol')
    print 'Current details: '
    gets_info_current = current_info_all[0].findAll('li')
    x = 1
    for each in gets_info_current:
        print str(x) + ': ' + str(each.text)
        x = x + 1

    print ''
    print '-----------------------------------------------------------------'
    print ''

if (extra_info[0].findChildren('tr', attrs={'data-section': 'pastPositionsDetails'})):
    past_info = extra_info[0].findChildren('tr', attrs={'data-section': 'pastPositionsDetails'})
    past_info_all = past_info[0].findChildren('ol')
    print 'Past details: '
    gets_info_past = past_info_all[0].findAll('li')
    x = 1
    for each in gets_info_past:
        print str(x) + ': ' + str(each.text)
        x = x + 1

    print ''
    print '-----------------------------------------------------------------'
    print ''

# Education section starts here
if (profile[0].findChildren('section', attrs={'id': 'education'})):
    profile_section_sch = profile[0].findChildren('section', attrs={'id': 'education'})
    profile_section_school = profile_section_sch[0].find('h3', attrs={'class': 'title'}).text
    print profile_section_school + ': '

    profile_section_education = profile_section_sch[0].findChildren('ul', attrs={'class': 'schools'})

    x = 1
    iteredu = iter(profile_section_education[0].findChildren('li'))
    for li in iteredu:
        print str(x) + ':',
        if (li.findChildren('h4', attrs={'class': 'item-title'})):
            print li.find('h4', attrs={'class': 'item-title'}).text

        if (li.findChildren('h5', attrs={'class': 'item-subtitle'})):
            print li.find('h5', attrs={'class': 'item-subtitle'}).text

        if (li.findChildren('p', attrs={'class': 'description'})):
            des = li.find('p', attrs={'class': 'description'}).contents[0]
            print str(des)

        if (li.findChildren('div', attrs={'class': 'description'})):
            print li.find('div', attrs={'class': 'description'}).text

        x = x + 1
        print ''

    print '-----------------------------------------------------------------'
    print ''

# Summary section stars from here
if (profile[0].findChildren('section', attrs={'id': 'summary'})):
    summary = profile[0].findChildren('section', attrs={'id': 'summary'})
    summary_title = summary[0].find('h3', attrs={'class': 'title'}).text
    print summary_title
    summary_description = summary[0].find('div', attrs={'class': 'description'}).text
    print summary_description
    print ''
    print '-----------------------------------------------------------------'
    print ''

# Experience section starts from here
if (profile[0].findChildren('section', attrs={'id': 'experience'})):
    profile_section_exp = profile[0].findChildren('section', attrs={'id': 'experience'})
    profile_section_experience = profile_section_exp[0].find('h3', attrs={'class': 'title'}).text
    print profile_section_experience + ': '

    profile_section_positions = profile_section_exp[0].findChildren('ul', attrs={'class': 'positions'})

    x = 1
    iterexp = iter(profile_section_positions[0].findChildren('li'))
    for li in iterexp:
        print str(x) + ':',
        if (li.findChildren('h4', attrs={'class': 'item-title'})):
            print li.find('h4', attrs={'class': 'item-title'}).text

        if (li.findChildren('h5', attrs={'class': 'item-subtitle'})):
            print li.find('h5', attrs={'class': 'item-subtitle'}).text

        if (li.findChildren('p', attrs={'class': 'description'})):
            des = li.find('p', attrs={'class': 'description'}).contents[0]
            print str(des)

        if (li.findChildren('div', attrs={'class': 'description'})):
            print li.find('div', attrs={'class': 'description'}).text

        print ''
        x = x + 1

    print '-----------------------------------------------------------------'
    print ''

# Certificate section starts from here
if (profile[0].findChildren('section', attrs={'id': 'certifications'})):
    profile_section_cer = profile[0].findChildren('section', attrs={'id': 'certifications'})
    profile_section_certificate = profile_section_cer[0].find('h3', attrs={'class': 'title'}).text
    print profile_section_certificate + ': '

    profile_section_certifications = profile_section_cer[0].findChildren('ul', attrs={'class': 'certifications'})

    x = 1
    itercer = iter(profile_section_certifications[0].findChildren('li'))
    for li in itercer:
        print str(x) + ':',
        if (li.findChildren('h4', attrs={'class': 'item-title'})):
            print li.find('h4', attrs={'class': 'item-title'}).text

        if (li.findChildren('h5', attrs={'class': 'item-subtitle'})):
            print li.find('h5', attrs={'class': 'item-subtitle'}).text

        if (li.findChildren('p', attrs={'class': 'description'})):
            des = li.find('p', attrs={'class': 'description'}).contents[0]
            print str(des)

        if (li.findChildren('div', attrs={'class': 'description'})):
            print li.find('div', attrs={'class': 'description'}).text

        x = x + 1
        print ''

    print '-----------------------------------------------------------------'
    print ''

# Projects section starts here
if (profile[0].findChildren('section', attrs={'id': 'projects'})):
    profile_section_prj = profile[0].findChildren('section', attrs={'id': 'projects'})
    profile_section_projects = profile_section_prj[0].find('h3', attrs={'class': 'title'}).text
    print profile_section_projects + ': '

    profile_section_project = profile_section_prj[0].findChildren('ul')

    x = 1
    iterproj = iter(profile_section_project[0].findChildren('li', attrs={'class': 'project'}))
    for li in iterproj:
        print str(x) + ':',
        if (li.findChildren('h4', attrs={'class': 'item-title'})):
            print li.find('h4', attrs={'class': 'item-title'}).text

        if (li.findChildren('h5', attrs={'class': 'item-subtitle'})):
            print li.find('h5', attrs={'class': 'item-subtitle'}).text

        if (li.findChildren('p', attrs={'class': 'description'})):
            des = li.find('p', attrs={'class': 'description'}).contents[0]
            print str(des)

        if (li.findChildren('div', attrs={'class': 'description'})):
            print li.find('div', attrs={'class': 'description'}).text

        if (li.findChildren('dl', attrs={'class': 'contributors'})):
            team_members = li.findChildren('dl')
            print team_members[0].find('dt').text
            team_members_all = team_members[0].findChildren('dd')
            c = 1
            itermem = iter(team_members_all[0].findChildren('li', 'contributor'))
            for each in itermem:
                print str(c) + ':',
                print each.text
                c = c + 1

        x = x + 1
        print ''

    print '-----------------------------------------------------------------'
    print ''

# Awards section starts from here
if (profile[0].findChildren('section', attrs={'id': 'awards'})):
    profile_section_awd = profile[0].findChildren('section', attrs={'id': 'awards'})
    profile_section_awards = profile_section_awd[0].find('h3', attrs={'class': 'title'}).text
    print profile_section_awards + ': '

    profile_section_user_awards = profile_section_awd[0].findChildren('ul')

    x = 1
    iterawd = iter(profile_section_user_awards[0].findChildren('li'))
    for li in iterawd:
        print str(x) + ':',
        if (li.findChildren('h4', attrs={'class': 'item-title'})):
            print li.find('h4', attrs={'class': 'item-title'}).text

        if (li.findChildren('h5', attrs={'class': 'item-subtitle'})):
            print li.find('h5', attrs={'class': 'item-subtitle'}).text

        if (li.findChildren('p', attrs={'class': 'description'})):
            des = li.find('p', attrs={'class': 'description'}).contents[0]
            print str(des)

        if (li.findChildren('div', attrs={'class': 'description'})):
            print li.find('div', attrs={'class': 'description'}).text

        print ''
        x = x + 1

    print '-----------------------------------------------------------------'
    print ''

# Skills section starts from here
if (profile[0].findChildren('section', attrs={'data-section': 'skills'})):
    skills = profile[0].findChildren('section', attrs={'data-section': 'skills'})
    skills_info = skills[0].find('h3', attrs={'class': 'title'}).text
    print skills_info + ': '
    skills_info_all = skills[0].findChildren('ul', attrs={'class': 'pills'})
    gets_info_current = skills_info_all[0].findAll('li')
    x = 1
    for each in gets_info_current:
        print str(x) + ': ' + str(each.text)
        x = x + 1

    print '-----------------------------------------------------------------'
    print ''

# Volunteering section starts here
if (profile[0].findChildren('section', attrs={'id': 'volunteering'})):
    profile_section_vol = profile[0].findChildren('section', attrs={'id': 'volunteering'})
    profile_section_volunteer = profile_section_vol[0].find('h3', attrs={'class': 'title'}).text
    print profile_section_volunteer + ': '

    profile_section_volunteering = profile_section_vol[0].findChildren('ul')

    x = 1
    itervol = iter(profile_section_volunteering[0].findChildren('li', attrs={'class': 'position'}))
    for li in itervol:
        print str(x) + ':',
        if (li.findChildren('h4', attrs={'class': 'item-title'})):
            print li.find('h4', attrs={'class': 'item-title'}).text

        if (li.findChildren('h5', attrs={'class': 'item-subtitle'})):
            print li.find('h5', attrs={'class': 'item-subtitle'}).text

        if (li.findChildren('p', attrs={'class': 'description'})):
            des = li.find('p', attrs={'class': 'description'}).contents[0]
            print str(des)

        if (li.findChildren('div', attrs={'class': 'description'})):
            print li.find('div', attrs={'class': 'description'}).text

        if (li.findChildren('dl', attrs={'class': 'contributors'})):
            team_members = li.findChildren('dl')
            print team_members[0].find('dt').text
            team_members_all = team_members[0].findChildren('dd')
            c = 1
            itermem = iter(team_members_all[0].findChildren('li', 'contributor'))
            for each in itermem:
                print str(c) + ':',
                print each.text
                c = c + 1

        x = x + 1
        print ''

    print '-----------------------------------------------------------------'
    print ''

# Publications section starts here
if (profile[0].findChildren('section', attrs={'id': 'publications'})):
    profile_section_pub = profile[0].findChildren('section', attrs={'id': 'publications'})
    profile_section_publication = profile_section_pub[0].find('h3', attrs={'class': 'title'}).text
    print profile_section_publication + ': '

    profile_section_publications = profile_section_pub[0].findChildren('ul')

    x = 1
    iterpub = iter(profile_section_publications[0].findChildren('li', attrs={'class': 'publication'}))
    for li in iterpub:
        print str(x) + ':',
        if (li.findChildren('h4', attrs={'class': 'item-title'})):
            print li.find('h4', attrs={'class': 'item-title'}).text

        if (li.findChildren('h5', attrs={'class': 'item-subtitle'})):
            print li.find('h5', attrs={'class': 'item-subtitle'}).text

        if (li.findChildren('span', attrs={'class': 'cause'})):
            print li.findChildren('span', attrs={'class': 'cause'}).text

        if (li.findChildren('p', attrs={'class': 'description'})):
            des = li.find('p', attrs={'class': 'description'}).contents[0]
            print str(des)

        if (li.findChildren('div', attrs={'class': 'description'})):
            print li.find('div', attrs={'class': 'description'}).text

        if (li.findChildren('dl', attrs={'class': 'contributors'})):
            team_members = li.findChildren('dl')
            print team_members[0].find('dt').text
            team_members_all = team_members[0].findChildren('dd')
            c = 1
            itermem = iter(team_members_all[0].findChildren('li', 'contributor'))
            for each in itermem:
                print str(c) + ':',
                print each.text
                c = c + 1

        x = x + 1
        print ''

    print '-----------------------------------------------------------------'
    print ''

# Languages section starts here
if (profile[0].findChildren('section', attrs={'id': 'languages'})):
    profile_section_lan = profile[0].findChildren('section', attrs={'id': 'languages'})
    profile_section_language = profile_section_lan[0].find('h3', attrs={'class': 'title'}).text
    print profile_section_language + ': '

    profile_section_languages = profile_section_lan[0].findChildren('ul')

    x = 1
    iterlan = iter(profile_section_languages[0].findChildren('li', attrs={'class': 'language'}))
    for li in iterlan:
        print str(x) + ':',
        if (li.findChildren('h4', attrs={'class': 'name'})):
            print li.find('h4', attrs={'class': 'name'}).text
        x = x + 1
        print ''

    print '-----------------------------------------------------------------'
    print ''

# Interests section starts here
if (profile[0].findChildren('section', attrs={'id': 'interests'})):
    profile_section_int = profile[0].findChildren('section', attrs={'id': 'interests'})
    profile_section_interest = profile_section_int[0].find('h3', attrs={'class': 'title'}).text
    print profile_section_interest + ': '

    profile_section_intrests = profile_section_int[0].findChildren('ul')

    x = 1
    iterint = iter(profile_section_intrests[0].findChildren('li', attrs={'class': 'interest'}))
    for li in iterint:
        print str(x) + ':',
        if (li.findChildren('span', attrs={'class': 'wrap'})):
            print li.find('span', attrs={'class': 'wrap'}).text
        x = x + 1
        print ''

    print '-----------------------------------------------------------------'
    print ''
