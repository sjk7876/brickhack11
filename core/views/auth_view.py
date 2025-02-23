import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login

oauth = OAuth()
User = get_user_model()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
)

def choose_user_type(request):
    user_id = request.session.get("pending_user_id")
    if not user_id:
        return redirect("index")

    user = User.objects.get(id=user_id)
    print("request.method:", request.method)

    if request.method == "POST":
        user_type = request.POST.get("user_type")
        if user_type in dict(User.USER_TYPE_CHOICES):
            user.user_type = user_type
            user.save()  # This saves the user type in the database.
            del request.session["pending_user_id"]
            auth_login(request, user)
            return redirect("index")

    return render(request, "choose_user_type.html", {"user": user})

def callback(request):
    # token = oauth.auth0.authorize_access_token(request)
    # request.session["user"] = token
    # user = User.objects.create_user(token["userinfo"]["given_name"], token["userinfo"]["email"], token["id_token"])
    # user.save()
    # return redirect(request.build_absolute_uri(reverse("index")))
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    user_info = token.get("userinfo", {})

    email = user_info.get("email")
    username = user_info.get("nickname", email.split("@")[0])  # Fallback to email prefix

    # Try to retrieve the user; if not found, create a new one.
    user, created = User.objects.get_or_create(email=email, defaults={"username": username})

    if created:
        # For new users, store the user id in session so we can set their user type
        request.session["pending_user_id"] = user.id
        print("pending user id:", request.session["pending_user_id"])
        # return redirect(request.build_absolute_uri(reverse("choose_user_type")))
        return redirect(reverse("choose_user_type"))

    # For returning users, log them in directly.
    auth_login(request, user)
    # return redirect(request.build_absolute_uri(reverse("index")))
    return redirect(reverse("index"))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                # "returnTo": request.build_absolute_uri(reverse("index")),
                "returnTo": reverse("index"),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
)

def index(request):
    return render(
        request,
        "home.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
)

def login_redirect(request):
    return redirect(request.build_absolute_uri(reverse("login")))