## [WIP]

In this project we are going to create a frontend in Vue and two backends with Go and Python to process images and extract text.

## Install

### MacOs
```bash
brew install tesseract opencv node python3 go
```

### Linux

#### Manjaro / Arch Linux based
```bash
sudo pacman -S tesseract opencv nodejs python3 go hdf5 vtk jsoncpp pugixml glew fmt
```

#### Debian / Ubuntu based
```bash
sudo apt install tesseract opencv nodejs python3 golang-go
```

#### Fedora / Red hat based
```bash
sudo dnf install tesseract opencv nodejs python3 golang
```

## Run

### Python
```bash
cd python/
python main.py
```

### Go
```bash
cd go/
go run main.go
```