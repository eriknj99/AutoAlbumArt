# AutoAlbumArt

A simple python script for applying album artwork to mp3 files.

#Usage
- Run with "python setAlbumArt.py"
- Enter a scan directory. All subdirectories of the san directory will be searched recursively.
- Enter image keys as CSV. Enter all album art names separated by commas. 
- The script will search for any album art in scan directory and apply it to any adjacent mp3 files

#Example
```
Music directory 

~
└── Music
    ├── Artist1
    │   ├── 1.mp3
    │   ├── 2.mp3
    │   ├── 3.mp3
    │   ├── 4.mp3
    │   └── cover.png
    └── Artist2
        ├── 1.mp3
        ├── 2.mp3
        ├── 3.mp3
        ├── 4.mp3
        └── cover.jpg
```
To apply album art to all mp3s in ~/Music run:
```
  python setAlbumArt.py
    Enter scan directory: ~/Muisc/
    Enter image keys as CSV: cover.png,cover.jpg
```
Album artwork will be applied to all .mp3 files in the Music directory.

#Dependencies  
- eyed3
- csv
- os
  
 
