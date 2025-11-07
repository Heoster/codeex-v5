<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- SEO Meta Tags -->
    <title>Codeex AI Chat - Professional Ollama Desktop Interface with Voice & Smart Model Management</title>
    <meta name="description" content="The most advanced open-source Ollama GUI client with auto-setup, text-to-speech, smart model management, and beautiful dark UI. Support for 20+ AI models including Llama3, Phi3, Gemma, Mistral. Free and cross-platform.">
    <meta name="keywords" content="Ollama GUI, AI chat, Llama3, Phi3, Gemma, Mistral, text to speech, chatbot, LLM interface, model management, Python GUI, CustomTkinter, open source AI, AI assistant, voice chat, cross-platform, desktop AI">
    <meta name="author" content="heoster">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://heoster.github.io/codeex-v5">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://heoster.github.io/codeex-v5">
    <meta property="og:title" content="Codeex AI Chat - Professional Ollama Desktop Interface">
    <meta property="og:description" content="The most advanced open-source Ollama GUI with auto-setup, voice synthesis, and smart model management. Support for 20+ AI models.">
    <meta property="og:image" content="https://heoster.github.io/codeex-v5/assets/og-image.png">
    <meta property="og:site_name" content="Codeex AI Chat">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://heoster.github.io/codeex-v5">
    <meta property="twitter:title" content="Codeex AI Chat - Professional Ollama Desktop Interface">
    <meta property="twitter:description" content="The most advanced open-source Ollama GUI with auto-setup, voice synthesis, and smart model management.">
    <meta property="twitter:image" content="https://heoster.github.io/codeex-v5/assets/twitter-image.png">
    <meta property="twitter:creator" content="@codeex_heoster">
    
    <!-- Additional Meta Tags -->
    <meta name="theme-color" content="#1e3a8a">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    
    <!-- Favicon -->
    <link rel="icon" type="image/png" href="favicon.png">
    <link rel="apple-touch-icon" href="apple-touch-icon.png">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    
    <!-- Schema.org markup for Google -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Codeex AI Chat",
      "description": "Professional Ollama desktop interface with auto-setup, text-to-speech, and smart model management. Support for 20+ AI models including Llama3, Phi3, Gemma, and Mistral.",
      "applicationCategory": "DeveloperApplication",
      "operatingSystem": "Windows, macOS, Linux",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      },
      "author": {
        "@type": "Person",
        "name": "heoster",
        "email": "codeex.care@gmail.com"
      },
      "datePublished": "2024-01-01",
      "softwareVersion": "5.0.0",
      "url": "https://heoster.github.io/codeex-v5",
      "screenshot": "https://heoster.github.io/codeex-v5/assets/screenshot.png",
      "downloadUrl": "https://github.com/heoster/codeex-v5/archive/refs/heads/main.zip",
      "codeRepository": "https://github.com/heoster/codeex-v5",
      "programmingLanguage": "Python",
      "license": "https://opensource.org/licenses/MIT",
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "100"
      }
    }
    </script>
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #1e3a8a;
            --secondary: #3b82f6;
            --accent: #60a5fa;
            --dark: #0f172a;
            --darker: #020617;
            --light: #f8fafc;
            --success: #059669;
            --gradient: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 50%, #60a5fa 100%);
        }

        body {
            font-family: 'Inter', sans-serif;
            background: var(--darker);
            color: var(--light);
            overflow-x: hidden;
            line-height: 1.6;
        }

        /* Animated Background */
        .bg-animation {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: linear-gradient(45deg, #0f172a, #1e293b, #334155);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
        }

        .stars {
            position: fixed;
            width: 100%;
            height: 100%;
            z-index: -1;
        }

        .star {
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            animation: twinkle 3s infinite;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1; }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }

        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        @keyframes glow {
            0%, 100% { box-shadow: 0 0 20px rgba(59, 130, 246, 0.3); }
            50% { box-shadow: 0 0 40px rgba(59, 130, 246, 0.6); }
        }

        /* Header */
        header {
            background: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(20px);
            padding: 1.5rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid rgba(59, 130, 246, 0.3);
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
        }

        nav {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
        }

        .logo {
            font-family: 'Orbitron', sans-serif;
            font-size: 2rem;
            font-weight: 900;
            background: var(--gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(59, 130, 246, 0.5);
            animation: pulse 2s infinite;
            cursor: pointer;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .nav-links a {
            color: var(--light);
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
            position: relative;
        }

        .nav-links a:hover {
            color: var(--accent);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--gradient);
            transition: width 0.3s;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* Mobile Menu */
        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            color: var(--light);
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 8rem 2rem 4rem;
            position: relative;
        }

        .hero-content {
            max-width: 1200px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }

        .hero-text {
            animation: slideInRight 1s ease-out;
        }

        .hero h1 {
            font-family: 'Orbitron', sans-serif;
            font-size: 3.5rem;
            font-weight: 900;
            margin-bottom: 1rem;
            background: var(--gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.2;
        }

        .hero h2 {
            font-size: 1.8rem;
            color: var(--accent);
            margin-bottom: 1.5rem;
            font-weight: 600;
        }

        .hero p {
            font-size: 1.2rem;
            color: #94a3b8;
            margin-bottom: 2rem;
        }

        .badges {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-bottom: 2rem;
        }

        .badge {
            background: rgba(59, 130, 246, 0.1);
            border: 1px solid var(--secondary);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            color: var(--accent);
            font-weight: 600;
        }

        .cta-buttons {
            display: flex;
            gap: 1.5rem;
            flex-wrap: wrap;
        }

        .btn {
            padding: 1rem 2.5rem;
            border-radius: 50px;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1.1rem;
            border: none;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }

        .btn:hover::before {
            width: 300px;
            height: 300px;
        }

        .btn-primary {
            background: var(--gradient);
            color: white;
            box-shadow: 0 10px 40px rgba(59, 130, 246, 0.4);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 50px rgba(59, 130, 246, 0.6);
        }

        .btn-secondary {
            background: rgba(59, 130, 246, 0.1);
            border: 2px solid var(--secondary);
            color: var(--accent);
        }

        .btn-secondary:hover {
            background: rgba(59, 130, 246, 0.2);
            transform: translateY(-3px);
        }

        /* 3D Card */
        .hero-visual {
            perspective: 1000px;
            animation: slideInUp 1s ease-out;
        }

        .demo-card {
            background: rgba(30, 41, 59, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            border: 1px solid rgba(59, 130, 246, 0.3);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            transform-style: preserve-3d;
            animation: float 3s ease-in-out infinite, glow 3s ease-in-out infinite;
        }

        .demo-card-header {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }

        .demo-card-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--accent);
            animation: pulse 2s infinite;
        }

        /* Stats Section */
        .stats {
            padding: 4rem 2rem;
            background: rgba(30, 41, 59, 0.3);
        }

        .stats-grid {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
        }

        .stat-card {
            text-align: center;
            padding: 2rem;
            background: rgba(30, 41, 59, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            border: 1px solid rgba(59, 130, 246, 0.3);
            transition: all 0.3s;
        }

        .stat-card:hover {
            transform: translateY(-10px);
            border-color: var(--accent);
        }

        .stat-number {
            font-family: 'Orbitron', sans-serif;
            font-size: 3rem;
            font-weight: 900;
            background: var(--gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .stat-label {
            color: #94a3b8;
            font-size: 1rem;
            margin-top: 0.5rem;
        }

        /* Features Section */
        .features {
            padding: 6rem 2rem;
            background: rgba(15, 23, 42, 0.5);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-title {
            text-align: center;
            margin-bottom: 4rem;
        }

        .section-title h2 {
            font-family: 'Orbitron', sans-serif;
            font-size: 3rem;
            background: var(--gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }

        .section-title p {
            font-size: 1.2rem;
            color: #94a3b8;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2rem;
        }

        .feature-card {
            background: rgba(30, 41, 59, 0.6);
            backdrop-filter: blur(10px);
            padding: 2.5rem;
            border-radius: 15px;
            border: 1px solid rgba(59, 130, 246, 0.3);
            transition: all 0.3s;
            cursor: pointer;
        }

        .feature-card:hover {
            transform: translateY(-10px);
            border-color: var(--accent);
            box-shadow: 0 20px 60px rgba(59, 130, 246, 0.3);
        }

        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1.5rem;
            display: block;
        }

        .feature-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--accent);
        }

        .feature-card p {
            color: #94a3b8;
            line-height: 1.8;
        }

        .feature-list {
            list-style: none;
            margin-top: 1rem;
        }

        .feature-list li {
            padding: 0.5rem 0;
            padding-left: 1.5rem;
            position: relative;
            color: #cbd5e1;
        }

        .feature-list li::before {
            content: '✓';
            position: absolute;
            left: 0;
            color: var(--success);
            font-weight: bold;
        }

        /* Models Showcase */
        .models-showcase {
            padding: 6rem 2rem;
            background: rgba(30, 41, 59, 0.3);
        }

        .models-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            margin-top: 3rem;
        }

        .model-category {
            background: rgba(30, 41, 59, 0.6);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 15px;
            border-left: 4px solid var(--secondary);
            transition: all 0.3s;
        }

        .model-category:hover {
            transform: translateX(10px);
            border-left-color: var(--accent);
        }

        .model-category h4 {
            color: var(--accent);
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }

        .model-category ul {
            list-style: none;
        }

        .model-category li {
            padding: 0.5rem 0;
            color: #cbd5e1;
            font-family: 'Courier New', monospace;
        }

        /* Installation Section */
        .installation {
            padding: 6rem 2rem;
            background: rgba(15, 23, 42, 0.5);
        }

        .steps-grid {
            display: grid;
            gap: 2rem;
            margin-top: 3rem;
        }

        .step {
            background: rgba(30, 41, 59, 0.6);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 15px;
            border-left: 4px solid var(--secondary);
            transition: all 0.3s;
        }

        .step:hover {
            border-left-color: var(--accent);
            transform: translateX(10px);
        }

        .step-number {
            display: inline-block;
            width: 50px;
            height: 50px;
            background: var(--gradient);
            border-radius: 50%;
            text-align: center;
            line-height: 50px;
            font-weight: 900;
            margin-bottom: 1rem;
            font-family: 'Orbitron', sans-serif;
            font-size: 1.5rem;
        }

        .step h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--accent);
        }

        .code-block {
            background: rgba(0, 0, 0, 0.5);
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
            border: 1px solid rgba(59, 130, 246, 0.3);
            position: relative;
            overflow-x: auto;
        }

        .code-block code {
            color: #10b981;
            font-family: 'Courier New', monospace;
            font-size: 0.95rem;
        }

        .copy-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background: var(--secondary);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.85rem;
            transition: all 0.3s;
        }

        .copy-btn:hover {
            background: var(--accent);
            transform: scale(1.05);
        }

        /* System Requirements */
        .requirements {
            padding: 6rem 2rem;
            background: rgba(30, 41, 59, 0.3);
        }

        .req-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .req-card {
            background: rgba(30, 41, 59, 0.6);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            border: 1px solid rgba(59, 130, 246, 0.3);
            transition: all 0.3s;
        }

        .req-card:hover {
            transform: scale(1.05);
            border-color: var(--accent);
        }

        .req-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .req-card h4 {
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
            color: var(--accent);
        }

        .req-card p {
            color: #94a3b8;
        }

        /* Contact Section */
        .contact {
            padding: 6rem 2rem;
            background: rgba(15, 23, 42, 0.5);
        }

        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .contact-card {
            background: rgba(30, 41, 59, 0.6);
            backdrop-filter: blur(10px);
            padding: 2.5rem;
            border-radius: 15px;
            border: 1px solid rgba(59, 130, 246, 0.3);
            text-align: center;
            transition: all 0.3s;
        }

        .contact-card:hover {
            transform: translateY(-10px);
            border-color: var(--accent);
            box-shadow: 0 20px 60px rgba(59, 130, 246, 0.3);
        }

        .contact-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .contact-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--accent);
        }

        .contact-card a {
            color: var(--light);
            text-decoration: none;
            transition: color 0.3s;
        }

        .contact-card a:hover {
            color: var(--accent);
        }

        /* Footer */
        footer {
            background: rgba(2, 6, 23, 0.9);
            backdrop-filter: blur(10px);
            padding: 3rem 2rem 1.5rem;
            border-top: 1px solid rgba(59, 130, 246, 0.3);
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
        }

        .footer-logo {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.5rem;
            background: var(--gradient);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin: 2rem 0;
            flex-wrap: wrap;
        }

        .footer-links a {
            color: var(--light);
            text-decoration: none;
            transition: color 0.3s;
        }

        .footer-links a:hover {
            color: var(--accent);
        }

        .copyright {
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(59, 130, 246, 0.2);
            color: #64748b;
        }

        .made-by {
            margin-top: 1rem;
            font-size: 1.1rem;
            color: var(--accent);
        }

        /* Responsive */
        @media (max-width: 768px) {
            .hero-content {
                grid-template-columns: 1fr;
            }

            .hero h1 {
                font-size: 2.5rem;
            }

            .nav-links {
                display: none;
            }

            .mobile-menu-btn {
                display: block;
            }

            .cta-buttons {
                flex-direction: column;
            }

            .section-title h2 {
                font-size: 2rem;
            }

            .features-grid,
            .models-grid,
            .req-grid,
            .contact-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Scroll animations */
        .fade-in {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.6s ease-out;
        }

        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* Floating particles */
        .particle {
            position: fixed;
            width: 4px;
            height: 4px;
            background: var(--accent);
            border-radius: 50%;
            pointer-events: none;
            opacity: 0.5;
            animation: rise 10s linear infinite;
        }

        @keyframes rise {
            0% {
                transform: translateY(0) rotate(0deg);
                opacity: 0;
            }
            10% {
                opacity: 0.5;
            }
            100% {
                transform: translateY(-100vh) rotate(360deg);
                opacity: 0;
            }
        }

        /* Comparison Table */
        .comparison-table {
            margin: 3rem 0;
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background: rgba(30, 41, 59, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            overflow: hidden;
        }

        th, td {
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid rgba(59, 130, 246, 0.2);
        }

        th {
            background: var(--gradient);
            color: white;
            font-weight: 700;
        }

        td {
            color: #cbd5e1;
        }

        .check {
            color: var(--success);
            font-weight: bold;
        }

        .cross {
            color: #ef4444;
            font-weight: bold;
        }

        /* Back to Top Button */
        .back-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: var(--gradient);
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            opacity: 0;
            transition: all 0.3s;
            z-index: 999;
            box-shadow: 0 4px 20px rgba(59, 130, 246, 0.4);
        }

        .back-to-top.visible {
            opacity: 1;
        }

        .back-to-top:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(59, 130, 246, 0.6);
        }
    </style>
</head>
<body>
    <!-- Animated Background -->
    <div class="bg-animation"></div>
    <div class="stars" id="stars"></div>

    <!-- Header -->
    <header>
        <nav>
            <div class="logo" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">⚡ CODEEX</div>
            <ul class="nav-links">
                <li><a href="#features">Features</a></li>
                <li><a href="#models">Models</a></li>
                <li><a href="#installation">Installation</a></li>
                <li><a href="#requirements">Requirements</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <button class="mobile-menu-btn">☰</button>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <div class="hero-text">
                <h1>CODEEX AI CHAT</h1>
                <h2>Professional Ollama Interface</h2>
                <div class="badges">
                    <span class="badge">🚀 Auto-Setup</span>
                    <span class="badge">🎙️ Text-to-Speech</span>
                    <span class="badge">🤖 20+ Models</span>
                    <span class="badge">💾 Save/Load</span>
                    <span class="badge">🆓 Open Source</span>
                </div>
                <p>Experience the next generation of AI chat with advanced features, beautiful UI, and seamless model management. Built with ❤️ for developers and AI enthusiasts.</p>
                <div class="cta-buttons">
                    <a href="https://github.com/heoster/codeex-v5" class="btn btn-primary" target="_blank" rel="noopener">
                        ⭐ Star on GitHub
                    </a>
                    <a href="#installation" class="btn btn-secondary">
                        📥 Get Started
                    </a>
                    <a href="https://github.com/heoster/codeex-v5/archive/refs/heads/main.zip" class="btn btn-secondary" rel="noopener">
                        💾 Download ZIP
                    </a>
                </div>
            </div>
            <div class="hero-visual">
                <div class="demo-card">
                    <div class="demo-card-header">
                        <div class="demo-card-dot"></div>
                        <h3 style="color: var(--accent); margin: 0;">🤖 AI-Powered Chat</h3>
                    </div>
                    <div style="background: rgba(0,0,0,0.3); padding: 1.5rem; border-radius: 10px; margin-bottom: 1rem;">
                        <p style="color: #60a5fa; margin-bottom: 0.5rem; font-weight: 600;">👤 You:</p>
                        <p style="color: #cbd5e1;">What can you do?</p>
                    </div>
                    <div style="background: rgba(5, 150, 105, 0.1); padding: 1.5rem; border-radius: 10px;">
                        <p style="color: #34d399; margin-bottom: 0.5rem; font-weight: 600;">🤖 Codeex AI:</p>
                        <p style="color: #cbd5e1;">I can help you with coding, answer questions, and much more! I support text-to-speech, model switching, and conversation management. ✨</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Stats Section -->
    <section class="stats fade-in">
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">20+</div>
                <div class="stat-label">AI Models Supported</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">0</div>
                <div class="stat-label">Manual Setup Steps</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">100%</div>
                <div class="stat-label">Free & Open Source</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">3</div>
                <div class="stat-label">Platforms Supported</div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="features fade-in" id="features">
        <div class="container">
            <div class="section-title">
                <h2>🚀 Powerful Features</h2>
                <p>Everything you need for professional AI conversations</p>
            </div>
            <div class="features-grid">
                <div class="feature-card">
                    <span class="feature-icon">⚡</span>
                    <h3>Auto-Start System</h3>
                    <p>Intelligent initialization that handles everything for you</p>
                    <ul class="feature-list">
                        <li>Auto-starts Ollama service</li>
                        <li>Auto-downloads models</li>
                        <li>Service health checks</li>
                        <li>Zero manual setup</li>
                    </ul>
                </div>

                <div class="feature-card">
                    <span class="feature-icon">🤖</span>
                    <h3>Smart Model Manager</h3>
                    <p>Intelligent model selection based on your system</p>
                    <ul class="feature-list">
                        <li>RAM-based recommendations</li>
                        <li>One-click downloads</li>
                        <li>20+ models available</li>
                        <li>Instant model switching</li>
                    </ul>
                </div>

                <div class="feature-card">
                    <span class="feature-icon">💬</span>
                    <h3>Advanced Chat</h3>
                    <p>Professional chat interface with real-time streaming</p>
                    <ul class="feature-list">
                        <li>Streaming responses</li>
                        <li>Context-aware AI</li>
                        <li>Message history</li>
                        <li>Beautiful formatting</li>
                    </ul>
                </div>

                <div class="feature-card">
                    <span class="feature-icon">🔊</span>
                    <h3>Text-to-Speech</h3>
                    <p>Hear AI responses with customizable voice settings</p>
                    <ul class="feature-list">
                        <li>Toggle TTS on/off</li>
                        <li>Adjustable speed (50-300 WPM)</li>
                        <li>Volume control (0-100%)</li>
                        <li>Auto-speak responses</li>
                    </ul>
                </div>

                <div class="feature-card">
                    <span class="feature-icon">💾</span>
                    <h3>Chat Management</h3>
                    <p>Save, load, and export your conversations</p>
                    <ul class="feature-list">
                        <li>Save conversations (JSON)</li>
                        <li>Load previous chats</li>
                        <li>Export to TXT</li>
                        <li>Quick access sidebar</li>
                    </ul>
                </div>

                <div class="feature-card">
                    <span class="feature-icon">🎨</span>
                    <h3>Professional UI</h3>
                    <p>Modern, dark-themed interface with Codeex branding</p>
                    <ul class="feature-list">
                        <li>Clean dark theme</li>
                        <li>Color-coded messages</li>
                        <li>Responsive design</li>
                        <li>Smooth animations</li>
                    </ul>
                </div>
            </div>

            <!-- Comparison Table -->
            <div class="comparison-table" style="margin-top: 4rem;">
                <h3 style="text-align: center; color: var(--accent); margin-bottom: 2rem; font-size: 2rem;">📊 Comparison with Other Solutions</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Feature</th>
                            <th>Codeex AI Chat</th>
                            <th>Ollama CLI</th>
                            <th>Other GUIs</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Auto-Start Ollama</td>
                            <td class="check">✅</td>
                            <td class="cross">❌</td>
                            <td>⚠️ Rare</td>
                        </tr>
                        <tr>
                            <td>Text-to-Speech</td>
                            <td class="check">✅</td>
                            <td class="cross">❌</td>
                            <td class="cross">❌</td>
                        </tr>
                        <tr>
                            <td>Smart Model Recommendations</td>
                            <td class="check">✅</td>
                            <td class="cross">❌</td>
                            <td class="cross">❌</td>
                        </tr>
                        <tr>
                            <td>One-Click Model Downloads</td>
                            <td class="check">✅</td>
                            <td>⚠️ Manual</td>
                            <td>⚠️ Limited</td>
                        </tr>
                        <tr>
                            <td>Save/Load Conversations</td>
                            <td class="check">✅</td>
                            <td class="cross">❌</td>
                            <td>⚠️ Basic</td>
                        </tr>
                        <tr>
                            <td>Export Chats</td>
                            <td class="check">✅</td>
                            <td class="cross">❌</td>
                            <td>⚠️ Rare</td>
                        </tr>
                        <tr>
                            <td>Real-time Streaming</td>
                            <td class="check">✅</td>
                            <td class="check">✅</td>
                            <td>⚠️ Some</td>
                        </tr>
                        <tr>
                            <td>Professional UI</td>
                            <td class="check">✅</td>
                            <td class="cross">❌</td>
                            <td>⚠️ Basic</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- Models Showcase -->
    <section class="models-showcase fade-in" id="models">
        <div class="container">
            <div class="section-title">
                <h2>🤖 Supported AI Models</h2>
                <p>20+ models optimized for different system configurations</p>
            </div>
            <div class="models-grid">
                <div class="model-category" style="border-left-color: #ef4444;">
                    <h4>💎 Tiny Models (< 8GB RAM)</h4>
                    <ul>
                        <li>phi3:mini - 3.8GB</li>
                        <li>tinyllama - 637MB</li>
                        <li>qwen2:0.5b - 352MB</li>
                    </ul>
                </div>
                <div class="model-category" style="border-left-color: #f59e0b;">
                    <h4>🔷 Small Models (8-16GB RAM)</h4>
                    <ul>
                        <li>llama3.2:1b - 1.3GB</li>
                        <li>gemma2:2b - 1.6GB</li>
                        <li>phi3:medium - 7.9GB</li>
                    </ul>
                </div>
                <div class="model-category" style="border-left-color: #3b82f6;">
                    <h4>🔶 Medium Models (16-32GB RAM)</h4>
                    <ul>
                        <li>llama3.2:3b - 2.0GB</li>
                        <li>gemma2:9b - 5.4GB</li>
                        <li>mistral - 4.1GB</li>
                        <li>qwen2.5:7b - 4.7GB</li>
                    </ul>
                </div>
                <div class="model-category" style="border-left-color: #10b981;">
                    <h4>🟢 Large Models (32GB+ RAM)</h4>
                    <ul>
                        <li>llama3.1:8b - 4.7GB</li>
                        <li>llama3:8b - 4.7GB</li>
                        <li>mixtral:8x7b - 26GB</li>
                    </ul>
                </div>
                <div class="model-category" style="border-left-color: #8b5cf6;">
                    <h4>🔴 XLarge Models (64GB+ RAM)</h4>
                    <ul>
                        <li>llama3.1:70b - 40GB</li>
                        <li>qwen2.5:72b - 41GB</li>
                    </ul>
                </div>
                <div class="model-category" style="border-left-color: #ec4899;">
                    <h4>💻 Specialized Models</h4>
                    <ul>
                        <li>codellama - Code assistant</li>
                        <li>deepseek-coder - Advanced coding</li>
                        <li>orca-mini - Reasoning</li>
                        <li>neural-chat - Conversations</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Installation Section -->
    <section class="installation fade-in" id="installation">
        <div class="container">
            <div class="section-title">
                <h2>📦 Quick Installation</h2>
                <p>Get started in just 3 simple steps</p>
            </div>
            <div class="steps-grid">
                <div class="step">
                    <span class="step-number">1</span>
                    <h3>Install Ollama</h3>
                    <p>Download and install Ollama from the official website:</p>
                    <div class="code-block">
                        <code>https://ollama.ai</code>
                        <button class="copy-btn" onclick="copyCode(this, 'https://ollama.ai')">Copy</button>
                    </div>
                    <p style="color: #94a3b8; margin-top: 1rem;">✅ Available for Windows, macOS, and Linux</p>
                </div>

                <div class="step">
                    <span class="step-number">2</span>
                    <h3>Install Python Dependencies</h3>
                    <p>Install required Python packages:</p>
                    <div class="code-block">
                        <code>pip install customtkinter pillow requests psutil pyttsx3</code>
                        <button class="copy-btn" onclick="copyCode(this, 'pip install customtkinter pillow requests psutil pyttsx3')">Copy</button>
                    </div>
                    <p style="color: #94a3b8; margin-top: 1rem;">✅ Python 3.8 or higher required</p>
                </div>

                <div class="step">
                    <span class="step-number">3</span>
                    <h3>Clone & Run</h3>
                    <p>Clone the repository and run the application:</p>
                    <div class="code-block">
                        <code>git clone https://github.com/heoster/codeex-v5.git<br>
cd codeex-v5<br>
python codeex_chat.py</code>
                        <button class="copy-btn" onclick="copyCode(this, 'git clone https://github.com/heoster/codeex-v5.git\ncd codeex-v5\npython codeex_chat.py')">Copy</button>
                    </div>
                    <p style="color: #94a3b8; margin-top: 1rem;">✅ The app will auto-start Ollama and download the default model!</p>
                </div>
            </div>

            <div style="margin-top: 3rem; text-align: center;">
                <h3 style="color: var(--accent); margin-bottom: 1rem;">Alternative: Download Directly</h3>
                <a href="https://github.com/heoster/codeex-v5/archive/refs/heads/main.zip" class="btn btn-primary">
                    📥 Download ZIP File
                </a>
            </div>
        </div>
    </section>

    <!-- System Requirements -->
    <section class="requirements fade-in" id="requirements">
        <div class="container">
            <div class="section-title">
                <h2>💻 System Requirements</h2>
                <p>Optimized for various system configurations</p>
            </div>
            <div class="req-grid">
                <div class="req-card">
                    <div class="req-icon">🖥️</div>
                    <h4>Operating System</h4>
                    <p>Windows 10/11<br>macOS 11+<br>Linux (Ubuntu, Debian, etc.)</p>
                </div>
                <div class="req-card">
                    <div class="req-icon">🧠</div>
                    <h4>RAM</h4>
                    <p>Minimum: 4GB<br>Recommended: 8GB+<br>Optimal: 16GB+</p>
                </div>
                <div class="req-card">
                    <div class="req-icon">🐍</div>
                    <h4>Python</h4>
                    <p>Version: 3.8 - 3.12<br>Required: pip<br>Virtual env recommended</p>
                </div>
                <div class="req-card">
                    <div class="req-icon">💾</div>
                    <h4>Storage</h4>
                    <p>App: ~50MB<br>Models: 500MB - 40GB<br>SSD recommended</p>
                </div>
            </div>

            <div style="margin-top: 3rem; background: rgba(30, 41, 59, 0.6); padding: 2rem; border-radius: 15px; border: 1px solid rgba(59, 130, 246, 0.3);">
                <h3 style="color: var(--accent); margin-bottom: 1.5rem; text-align: center;">📊 Model Recommendations by RAM</h3>
                <div style="display: grid; gap: 1rem;">
                    <div style="padding: 1rem; background: rgba(0,0,0,0.3); border-radius: 10px; border-left: 4px solid #ef4444;">
                        <strong style="color: #fca5a5;">< 8GB RAM:</strong> <span style="color: #cbd5e1;">phi3:mini, tinyllama, qwen2:0.5b</span>
                    </div>
                    <div style="padding: 1rem; background: rgba(0,0,0,0.3); border-radius: 10px; border-left: 4px solid #f59e0b;">
                        <strong style="color: #fcd34d;">8-16GB RAM:</strong> <span style="color: #cbd5e1;">llama3.2:1b, gemma2:2b, phi3:medium</span>
                    </div>
                    <div style="padding: 1rem; background: rgba(0,0,0,0.3); border-radius: 10px; border-left: 4px solid #3b82f6;">
                        <strong style="color: #93c5fd;">16-32GB RAM:</strong> <span style="color: #cbd5e1;">llama3.2:3b, gemma2:9b, mistral</span>
                    </div>
                    <div style="padding: 1rem; background: rgba(0,0,0,0.3); border-radius: 10px; border-left: 4px solid #10b981;">
                        <strong style="color: #6ee7b7;">32GB+ RAM:</strong> <span style="color: #cbd5e1;">llama3.1:8b, mixtral:8x7b, llama3:70b</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact fade-in" id="contact">
        <div class="container">
            <div class="section-title">
                <h2>📞 Get in Touch</h2>
                <p>Connect with us for support, feedback, or collaboration</p>
            </div>
            <div class="contact-grid">
                <div class="contact-card">
                    <div class="contact-icon">📧</div>
                    <h3>Email</h3>
                    <p><a href="mailto:codeex.care@gmail.com">codeex.care@gmail.com</a></p>
                    <p style="color: #64748b; font-size: 0.9rem; margin-top: 0.5rem;">For support and inquiries</p>
                </div>
                <div class="contact-card">
                    <div class="contact-icon">📸</div>
                    <h3>Instagram</h3>
                    <p><a href="https://instagram.com/codeex._.heoster" target="_blank" rel="noopener">@codeex._.heoster</a></p>
                    <p style="color: #64748b; font-size: 0.9rem; margin-top: 0.5rem;">Follow for updates</p>
                </div>
                <div class="contact-card">
                    <div class="contact-icon">⭐</div>
                    <h3>GitHub</h3>
                    <p><a href="https://github.com/heoster/codeex-v5" target="_blank" rel="noopener">heoster/codeex-v5</a></p>
                    <p style="color: #64748b; font-size: 0.9rem; margin-top: 0.5rem;">Star & contribute</p>
                </div>
            </div>

            <div style="margin-top: 3rem; text-align: center; background: rgba(30, 41, 59, 0.6); padding: 2rem; border-radius: 15px; border: 1px solid rgba(59, 130, 246, 0.3);">
                <h3 style="color: var(--accent); margin-bottom: 1rem;">🌟 Open Source & Free Forever</h3>
                <p style="color: #94a3b8; margin-bottom: 1.5rem;">
                    Codeex AI Chat is completely open source and free to use. <br>
                    Contributions, bug reports, and feature requests are welcome!
                </p>
                <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                    <a href="https://github.com/heoster/codeex-v5/issues" class="btn btn-secondary" target="_blank" rel="noopener">
                        🐛 Report Issue
                    </a>
                    <a href="https://github.com/heoster/codeex-v5/discussions" class="btn btn-secondary" target="_blank" rel="noopener">
                        💬 Discussions
                    </a>
                    <a href="https://github.com/heoster/codeex-v5/fork" class="btn btn-secondary" target="_blank" rel="noopener">
                        🍴 Fork Project
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-logo">⚡ CODEEX</div>
            <p style="color: #94a3b8; margin-bottom: 1.5rem;">
                Professional AI Chat Interface for Ollama<br>
                <strong>Made with ❤️ by heoster</strong>
            </p>
            <div class="footer-links">
                <a href="https://github.com/heoster/codeex-v5" target="_blank" rel="noopener">GitHub</a>
                <a href="https://instagram.com/codeex._.heoster" target="_blank" rel="noopener">Instagram</a>
                <a href="mailto:codeex.care@gmail.com">Email</a>
                <a href="https://ollama.ai" target="_blank" rel="noopener">Ollama</a>
                <a href="#features">Features</a>
                <a href="#installation">Installation</a>
            </div>
            <div class="copyright">
                <p>&copy; 2025 Codeex AI Chat. All rights reserved.</p>
                <p class="made-by">Created by <strong>heoster</strong> • MIT License</p>
                <p style="margin-top: 1rem; color: #64748b; font-size: 0.9rem;">
                    Powered by Ollama • Built with Python & CustomTkinter
                </p>
            </div>
        </div>
    </footer>

    <!-- Back to Top Button -->
    <div class="back-to-top" id="backToTop">
        ↑
    </div>

    <script>
        // Generate stars
        function createStars() {
            const starsContainer = document.getElementById('stars');
            const starCount = 100;

            for (let i = 0; i < starCount; i++) {
                const star = document.createElement('div');
                star.className = 'star';
                star.style.left = Math.random() * 100 + '%';
                star.style.top = Math.random() * 100 + '%';
                star.style.animationDelay = Math.random() * 3 + 's';
                starsContainer.appendChild(star);
            }
        }

        // Create floating particles
        function createParticles() {
            setInterval(() => {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.bottom = '-10px';
                document.body.appendChild(particle);

                setTimeout(() => {
                    particle.remove();
                }, 10000);
            }, 2000);
        }

        // Scroll animations
        function handleScrollAnimations() {
            const elements = document.querySelectorAll('.fade-in');
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                });
            }, { threshold: 0.1 });

            elements.forEach(element => {
                observer.observe(element);
            });
        }

        // Copy code function
        function copyCode(button, text) {
            navigator.clipboard.writeText(text).then(() => {
                const originalText = button.textContent;
                button.textContent = '✓ Copied!';
                button.style.background = '#059669';
                
                setTimeout(() => {
                    button.textContent = originalText;
                    button.style.background = '';
                }, 2000);
            });
        }

        // Smooth scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Back to top button
        const backToTop = document.getElementById('backToTop');
        
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        backToTop.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            createStars();
            createParticles();
            handleScrollAnimations();
        });

        // 3D card effect
        document.querySelectorAll('.demo-card').forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                
                const rotateX = (y - centerY) / 10;
                const rotateY = (centerX - x) / 10;
                
                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(10px)`;
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateZ(0)';
            });
        });

        // Track page views (Google Analytics placeholder)
        // Add your Google Analytics code here
    </script>
</body>
</html>
