# AmirBlog

This repo consist of customization of [BlogCity](https://github.com/Amine-Smahi/BlogCity).

I did this just for chanllenge. Actually i didn't know anything about C# and ASP.NET or .NET. but just for 36 hours i dived into it by learning and writing this prroject. (it was like Hakathon.)


---

> The goal is to create a secure multiuser platform for dynamic content. the user can:

- Create an account
- Login to own account
- Update hes credentials
- Add/edit/delete posts
- Create a profile page
- Watch other users posts
- Share posts on social media
- Social media authentication
- Like(love) posts
- Search for posts
- Download personnal data
- Two factor authentication

## How to run the project
The steps are very easy you only have to
* Check if .NET Core sdk version 2.2 preview2 installed on your system, you can download it from [Here](https://www.microsoft.com/net/download/dotnet-core/2.2) then check if the instalation has gone correctly by typing
      
      user$ dotnet --version
      user$ 2.2.100-preview2-009404
* Restore the dependencies by typing the commande
  
      user$ dotnet restore
* Apply migrations

      user$ dotnet ef database update
* Update Facebook app details

      user$ dotnet user-secrets set Authentication:Facebook:AppId <app-id>
      user$ dotnet user-secrets set Authentication:Facebook:AppSecret <app-secret>

* Finnaly go and run the app by typing

      user$ dotnet run