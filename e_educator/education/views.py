from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from education.models import author, user, lecture, city, state, country, course, course_order, exam, feedback, \
    question, subject_category, subject_subcategory, admin


# Create your views here.

def loaduser(request):
    return render(request, '../template/user.html', {})


def loadauthor(request):
    return render(request, '../template/author.html', {})


def loadadmin(request):
    return render(request, '../template/adminreg.html', {'msg': '', })

def load_e_educator(request):
    return render(request, '../template/commondesign_user.html', {'msg': '', })

def loadcategory(request):
    category_list = subject_category.objects.all()
    return render(request, '../template/subject_category.html', {'msg': '', 'category_list': category_list})

def loaduserregs(request):
    city_list= city.objects.all()
    return render(request, '../template/userreg.html', {'msg': '','city_list':city_list})

def loadsubcategory(request):
    subcategory_list = subject_subcategory.objects.all()
    category_list = subject_category.objects.all()
    return render(request, '../template/subject_subcategory.html',
                  {'msg': '', 'category_list': category_list, 'subcategory_list': subcategory_list})


def loadcountry(request):
    country_list = country.objects.all()
    return render(request, '../template/country.html', {'msg': '', 'country_list': country_list})


def loadstate(request):
    state_list = state.objects.all()
    country_list = country.objects.all()
    return render(request, '../template/state.html',
                  {'msg': '', 'state_list': state_list, 'country_list': country_list})


def loadcity(request):
    state_list = state.objects.all()
    city_list = city.objects.all()
    return render(request, '../template/city.html', {'msg': '', 'state_list': state_list, 'city_list': city_list})


def loadadminlogin(request):
    return render(request, '../template/adminlogin.html', {'msg': ''})


def loadforgotpassword(request):
    return render(request, '../template/ForgotPassword.html', {'msg': ''})


def loadadminregistration(request):
    return render(request, '../template/registration.html', {})


def addadmin(request):
    na = request.POST["fname"]
    pho = request.POST["phone"]
    mail = request.POST["mail"]
    pas = request.POST["pass"]
    c=admin.objects.filter(admin_emailid=mail).filter(admin_phone=pho)
    if len(c)!=0:
        return render(request, '../template/adminreg.html', {'msg': 'Email-id or     Mobile number Already added', })
    else:
        is_Active = 1
        ad = admin(admin_name=na, admin_phone=pho, admin_emailid=mail, admin_password=pas,
               admin_isActive=is_Active)
    ad.save()
    return render(request, '../template/adminlogin.html', {'msg': 'Admin added Sucessfully', })


def checkadminlogin(request):
    lx = request.POST["mail"]
    p = request.POST["pass"]
    r = admin.objects.filter(admin_emailid=lx).filter(admin_password=p)
    if len(r) == 0:
        return render(request, '../template/adminlogin.html', {'msg': 'Invalid Loginid or password'})
    else:
        country_list = country.objects.all()
        return render(request, '../template/country.html/', {'country_list': country_list})


def checkadminloginid(request):
    ma = request.POST["mail"]
    r = admin.objects.filter(admin_emailid=ma)

    if len(r) != 0:
        j = admin.objects.get(admin_emailid=ma)
        return render(request, '../template/recoverpassword.html', {'j': j})
    else:
        return render(request, '../template/ForgotPassword.html', {'msg':'Credential is Invalid or not found'})


def checkrecoverpassword(request):
    lid = request.POST["logid"]
    pas1 = request.POST["pass"]
    r = admin.objects.get(admin_emailid=lid)
    r.admin_password = pas1
    r.save()
    return render(request, '../template/adminlogin.html', {'msg': 'Password Changed Successful'})



def addcountry(request):
    coun = request.POST["country"]
    country_list = country.objects.all()
    l = country.objects.filter(name=coun)
    if len(l) != 0:
        country_list = country.objects.all()
        return render(request, '../template/country.html', {'msg': 'Country Already Added ','country_list': country_list})
    else:
        isActive = 1
        r = country(name=coun, con_isActive=isActive)
        r.save()
        return render(request, '../template/country.html',{'msg': 'Country adds Successfully', 'country_list': country_list})


def editcountry(request):
    iid = request.GET["x"]
    r = country.objects.get(id=iid)
    country_list = country.objects.all()
    return render(request, '../template/editcountry.html', {'msg': '', 'country_list': country_list, 'r': r})


def updatecountry(request):
    cid = request.POST["id"]
    coun = request.POST["countr"]
    r = country.objects.get(id=cid)
    r.name = coun
    r.con_isActive = 1
    r.save()
    country_list = country.objects.all()
    return render(request, '../template/country.html',
                  {'msg': 'Country Updated Successfully', 'country_list': country_list})


def deletecountry(request):
    id = request.GET["x"]
    r = country.objects.get(id=id)
    r.con_isActive = 0;
    r.save()
    country_list = country.objects.all()
    return render(request, '../template/country.html',
                  {'msg': 'Country Deleted Successfully', 'country_list': country_list})


def addstate(request):
    stat = request.POST["state"]
    cid = request.POST["countr"]
    cnt = country.objects.get(id=cid)
    state_list = state.objects.all()
    country_list = country.objects.all()
    l = state.objects.filter(name=stat)
    if len(l) != 0:
        return render(request, '../template/state.html',
                      {'msg': 'State Already Added ', 'country_list': country_list, 'state_list': state_list})
    else:
        isActive = 1;
        r = state(name=stat, countryid=cnt, sta_isActive=isActive)
        r.save()
        return render(request, '../template/state.html',
                      {'msg': 'State adds Successfully', 'country_list': country_list, 'state_list': state_list})


def editstate(request):
    iid = request.GET["x"]
    r = state.objects.get(id=iid)
    state_list = state.objects.all()
    country_list = country.objects.all()
    return render(request, '../template/editstate.html',
                  {'msg': '', 'country_list': country_list, 'state_list': state_list, 'r': r})


def updatestate(request):
    iid = request.POST["id"]
    stat = request.POST["state"]
    cid = request.POST["countr"]
    cnt = country.objects.get(id=cid)
    state_list = state.objects.all()
    country_list = country.objects.all()
    rs = state.objects.get(id=iid)
    rs.name = stat
    rs.countryid = cnt
    rs.sta_isActive = 1
    rs.save()
    return render(request, '../template/state.html',
                  {'msg': 'State Updated Successfully', 'country_list': country_list, 'state_list': state_list})


def deletestate(request):
    id = request.GET["x"]
    r = state.objects.get(id=id)
    r.sta_isActive = 0;
    r.save()
    state_list = state.objects.all()
    country_list = country.objects.all()
    return render(request, '../template/state.html',
                  {'msg': 'State Deleted Successfully', 'country_list': country_list, 'state_list': state_list})


def addcity(request):
    cit = request.POST["city"]
    sid = request.POST["state"]
    snt = state.objects.get(id=sid)
    state_list = state.objects.all()
    city_list = city.objects.all()
    l = city.objects.filter(name=cit)
    if len(l) != 0:
        return render(request, '../template/city.html',
                      {'msg': 'City Already Added ', 'city_list': city_list, 'state_list': state_list})
    else:
        isActive = 1;
        r = city(name=cit, stateid=snt, cit_isActive=isActive)
        r.save()
        return render(request, '../template/city.html',
                      {'msg': 'City adds Successfully', 'city_list': city_list, 'state_list': state_list})


def editcity(request):
    iid = request.GET["x"]
    r = city.objects.get(id=iid)
    state_list = state.objects.all()
    city_list = city.objects.all()
    return render(request, '../template/editcity.html',
                  {'msg': '', 'city_list': city_list, 'state_list': state_list, 'r': r})


def updatecity(request):
    iid = request.POST["id"]
    cit = request.POST["city"]
    sid = request.POST["state"]
    snt = state.objects.get(id=sid)
    state_list = state.objects.all()
    city_list = city.objects.all()
    rs = city.objects.get(id=iid)
    rs.name = cit
    rs.stateid = snt
    rs.cit_isActive = 1
    rs.save()
    return render(request, '../template/city.html',
                  {'msg': 'City Updated Successfully', 'city_list': city_list, 'state_list': state_list})


def deletecity(request):
    id = request.GET["x"]
    r = city.objects.get(id=id)
    r.cit_isActive = 0;
    r.save()
    state_list = state.objects.all()
    city_list = city.objects.all()
    return render(request, '../template/city.html',
                  {'msg': 'City Deleted Successfully', 'country_list': city_list, 'state_list': state_list})


def addcategory(request):
    cate = request.POST["cate"]
    category_list = subject_category.objects.all()
    l = subject_category.objects.filter(category_name=cate)
    if len(l) != 0:
        return render(request, '../template/subject_category.html',
                      {'msg': 'Category Already Added ', 'category_list': category_list})
    else:
        isActive = 1;
        r = subject_category(category_name=cate, cat_isActive=isActive)
        r.save()
        return render(request, '../template/subject_category.html',
                      {'msg': 'Category adds Successfully', 'category_list': category_list})


def editcategory(request):
    iid = request.GET["x"]
    r = subject_category.objects.get(id=iid)
    category_list = subject_category.objects.all()
    return render(request, '../template/editsubject_category.html', {'msg': '', 'category_list': category_list, 'r': r})


def updatecategory(request):
    iid = request.POST["id"]
    cate = request.POST["cate"]
    r = subject_category.objects.get(id=iid)
    r.category_name = cate
    r.cat_isActive = 1
    r.save()
    category_list = subject_category.objects.all()
    return render(request, '../template/subject_category.html',
                  {'msg': 'Category Updated Successfully', 'category_list': category_list})


def deletecategory(request):
    id = request.GET["x"]
    r = subject_category.objects.get(id=id)
    r.cat_isActive = 0;
    r.save()
    category_list = subject_category.objects.all()
    return render(request, '../template/subject_category.html',
                  {'msg': 'Category Deleted Successfully', 'category_list': category_list})


def addsubcategory(request):
    subcat = request.POST["subcat"]
    catid = request.POST["cat"]
    cnt = subject_category.objects.get(id=catid)
    photo = request.FILES["ph"]

    fs = FileSystemStorage()
    filename = fs.save(photo.name, photo)
    path = fs.url(filename)

    subcategory_list = subject_subcategory.objects.all()
    category_list = subject_category.objects.all()
    l = subject_subcategory.objects.filter(subcategory_name=subcat)

    if len(l) != 0:
        return render(request, '../template/subject_subcategory.html',
                      {'msg': 'Sub-Category Already Added ', 'category_list': category_list,
                       'subcategory_list': subcategory_list})
    else:
        isActive = 1;
        r = subject_subcategory(subcategory_name=subcat, categoryid=cnt, subcategory_photo=path,
                                subcategory_isActive=isActive)
        r.save()
        return render(request, '../template/subject_subcategory.html',
                      {'msg': 'Sub-Category adds Successfully', 'category_list': category_list,
                       'subcategory_list': subcategory_list})


def editsubcategory(request):
    iid = request.GET["x"]
    r = subject_subcategory.objects.get(id=iid)
    subcategory_list = subject_subcategory.objects.all()
    category_list = subject_category.objects.all()
    return render(request, '../template/editsubject_subcategory.html',
                  {'msg': '', 'r': r, 'category_list': category_list, 'subcategory_list': subcategory_list})


def updatesubcategory(request):
    iid = request.POST["sid"]
    subcat = request.POST["subcat"]
    catid = request.POST["cat"]

    cnt = subject_category.objects.get(id=catid)

    sb = subject_subcategory.objects.get(id=iid)
    sb.subcategory_name = subcat
    sb.categoryid = cnt

    if len(request.FILES) == 0:
        sb.subcategory_isActive = 1
        sb.save()
    else:
        photo = request.FILES["ph"]
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        path = fs.url(filename)
        sb.subcategory_photo = path
        sb.subcategory_isActive = 1
        sb.save()

    subcategory_list = subject_subcategory.objects.all()
    category_list = subject_category.objects.all()
    return render(request, '../template/subject_subcategory.html',
                  {'msg': 'Sub-Category Updated Successfully', 'category_list': category_list,
                   'subcategory_list': subcategory_list})


def deletesubcategory(request):
    id = request.GET["x"]
    r = subject_subcategory.objects.get(id=id)
    r.subcategory_isActive = 0;
    r.save()
    category_list = subject_category.objects.all()
    subcategory_list = subject_subcategory.objects.all()
    return render(request, '../template/subject_subcategory.html',
                  {'msg': 'Sub-Category Deleted Successfully', 'category_list': category_list,
                   'subcategory_list': subcategory_list})
