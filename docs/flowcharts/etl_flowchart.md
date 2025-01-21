```mermaid
flowchart TD
    A@{ shape: stadium, label: "Start: Data Sources"} --> B@{ shape: tri, label: "Extract Data"}
    B --> C{ shape: cyl, label: "Source: Medium API"}
    C --> D[Data Cleaning*]
    D --> E[Data Transformation**]
    E --> F[Load Transformed Data***]
    F --> G([Deploy Pipeline****])
```