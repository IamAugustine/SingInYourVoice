using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace Sing_In_Your_Voice
{
    /// <summary>
    /// Interaction logic for projMaker.xaml
    /// </summary>
    public partial class projMaker : Window
    {
        public projMaker()
        {
            InitializeComponent();
        }

        private void projFolder_dialog(object sender, RoutedEventArgs e)
        {
            // Configure open folder dialog box
            Microsoft.Win32.OpenFolderDialog dialog = new();

            dialog.Multiselect = false;
            dialog.Title = "Select a folder";

            // Show open folder dialog box
            bool? result = dialog.ShowDialog();

            // Process open folder dialog box results
            if (result == true)
            {
                // Get the selected folder
                string fullPathToFolder = dialog.FolderName;
                string folderNameOnly = dialog.SafeFolderName;
            }
        }

        private void returnHome(object sender, RoutedEventArgs e)
        {
            
        }
    }
}
