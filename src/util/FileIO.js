import React from "react";

export class FileIO extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            fileDownloadUrl: null,
            status: "",
        }
        this.download = this.download.bind(this);
        this.upload = this.upload.bind(this);
        this.openFile = this.openFile.bind(this);
    }

    download(event) {
        event.preventDefault();
        const output = this.props.dataFetcher();
        // Download it
        const blob = new Blob([output]);
        const fileDownloadUrl = URL.createObjectURL(blob);
        this.setState({fileDownloadUrl: fileDownloadUrl},
            () => {
                this.dofileDownload.click();
                URL.revokeObjectURL(fileDownloadUrl);  // free up storage--no longer needed.
                this.setState({fileDownloadUrl: ""})
            })
    }


    upload() {
        // event.preventDefault();
        // this.dofileUpload.click()
    }

    /**
     * Process the file within the React app. We're NOT uploading it to the server!
     */
    openFile(evt) {
        let status = []; // Status output
        const fileObj = evt.target.files[0];
        const reader = new FileReader();

        let fileloaded = e => {
            // e.target.result is the file's content as text
            const fileContents = e.target.result;
            status.push(`File name: "${fileObj.name}". Length: ${fileContents.length} bytes.`);
            // Show first 80 characters of the file
            this.props.onFileUpload(fileContents);
            const first80char = fileContents.substring(0, 80);
            status.push(`First 80 characters of the file:\n${first80char}`)
            this.setState({status: status.join("\n")})
        }

        // Mainline of the method
        fileloaded = fileloaded.bind(this);
        reader.onload = fileloaded;
        reader.readAsText(fileObj);
    }

    render() {
        return (
            <div>
                <a
                    style={{display: "none"}}
                    download={this.props.getFileName()}
                    href={this.state.fileDownloadUrl}
                    ref={e => this.dofileDownload = e}
                >download it</a>

                {
                    this.props.renderDlButton &&
                    this.props.renderDlButton(this.download)
                }

                {
                    this.props.renderUlButton && (
                        <input type="file" className="hidden"
                               multiple={false}
                               accept=".json,.csv,.txt,.text,application/json,text/csv,text/plain"
                               onChange={evt => this.openFile(evt)}
                               ref={e => this.dofileUpload = e}
                        />
                    )
                }
            </div>
        )
    }
}
