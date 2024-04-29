// Xamarin.Forms Kullanarak Basit Bir Uygulama

using Xamarin.Forms;

namespace OrnekUygulama
{
    public class App : Application
    {
        public App()
        {
            MainPage = new ContentPage
            {
                Content = new Label
                {
                    Text = "Merhaba Xamarin!",
                    HorizontalOptions = LayoutOptions.Center,
                    VerticalOptions = LayoutOptions.Center
                }
            };
        }
    }
}

