## docx => md with base64 images

### Build docker image
```docker build -t docx2md:latest .```

### Run 
```docker run --rm -v ${PWD}:/app/files -v ${PWD}/out:/app/out docx2md:latest <<docx file name>>```

output markdown file will show under ./out/