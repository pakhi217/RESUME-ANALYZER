async function uploadResume() {
    const fileInput = document.getElementById("resumeInput");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please upload a file first!");
        return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        document.getElementById("result").textContent =
            JSON.stringify(data, null, 2);

    } catch (error) {
        console.error(error);
        document.getElementById("result").textContent =
            "Error connecting to backend.";
    }
}