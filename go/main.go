package main

import (
	"bytes"
	"fmt"
	"image/png"

	"github.com/otiai10/gosseract"
	"gocv.io/x/gocv"
)

func preProcess(img gocv.Mat) gocv.Mat {
	grayImg := gocv.NewMat()
	gocv.CvtColor(img, &grayImg, gocv.ColorBGRToGray)
	threshImg := gocv.NewMat()
	gocv.Threshold(grayImg, &threshImg, 0.0, 255.0, gocv.ThresholdBinary|gocv.ThresholdOtsu)

	return grayImg
}

func postProcess(img gocv.Mat) (string, error) {
	client := gosseract.NewClient()
	defer client.Close()

	client.Languages = []string{"eng"}

	buf := new(bytes.Buffer)
	finalImage, err := img.ToImage()
	png.Encode(buf, finalImage)

	if err != nil {
		print(err)
	}

	client.SetImageFromBytes(buf.Bytes())
	client.SetPageSegMode(gosseract.PSM_AUTO)

	out, err := client.Text()

	if err != nil {
		return "", err
	}

	return out, nil
}

func main() {
	img := gocv.IMRead("../images/id1.jpg", gocv.IMReadColor)
	threshImg := preProcess(img)
	text, err := postProcess(threshImg)

	if err != nil {
		fmt.Println(err)
	}

	println(text)
}
