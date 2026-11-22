def get_css():
    return """
/* ==========================================================================
   EasyRail Design System & Base Variables
   ========================================================================== */
:root {
  --color-primary: #176B48;
  --color-primary-light: #1a7d55;
  --color-secondary: #E8F4EC;
  --color-bg: #F8FAF8;
  --color-text: #202923;
  --color-muted: #5a6b60;
  --color-border: #d0e4d6;
  --color-warning: #D99A25;
  --color-error: #C83D3D;
  --color-success: #18864B;
  --color-white: #ffffff;
  --radius: 16px;
  --radius-sm: 10px;
  --shadow: 0 2px 16px rgba(23,107,72,0.08);
  --shadow-lg: 0 8px 40px rgba(23,107,72,0.14);
  --font: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  
  --header-height: 72px;
  --transition: 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Base Reset & Typography */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-family: var(--font);
  font-size: 16px;
  scroll-behavior: smooth;
  background-color: var(--color-bg);
  color: var(--color-text);
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
  max-width: 100vw;
  width: 100%;
}

body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--color-bg);
  color: var(--color-text);
  line-height: 1.5;
  overflow-x: hidden;
  max-width: 100vw;
  width: 100%;
  position: relative;
}

a {
  color: var(--color-primary);
  text-decoration: none;
}

button, input, select, textarea {
  font-family: inherit;
  font-size: 1rem;
}

button {
  cursor: pointer;
  border: none;
  background: none;
  min-height: 44px;
  min-width: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all var(--transition);
}

button:focus-visible, input:focus-visible, select:focus-visible {
  outline: 3px solid var(--color-primary);
  outline-offset: 2px;
}

/* ==========================================================================
   Accessibility Mode (High Contrast & Large Font)
   ========================================================================== */
body.accessibility-mode {
  font-size: 120%;
  filter: contrast(1.2);
}

body.accessibility-mode * {
  transition: none !important;
  animation: none !important;
}

body.accessibility-mode .card,
body.accessibility-mode .search-card,
body.accessibility-mode .train-card,
body.accessibility-mode .class-card,
body.accessibility-mode .ticket-container {
  border: 2px solid #000000 !important;
  box-shadow: none !important;
}

body.accessibility-mode button,
body.accessibility-mode .btn {
  border: 2px solid #000000 !important;
}

.accessibility-banner {
  display: none;
  background: #111e15;
  color: #ffffff;
  padding: 10px 16px;
  font-size: 0.95rem;
  font-weight: 600;
  border-bottom: 2px solid var(--color-warning);
  position: sticky;
  top: 0;
  z-index: 1001;
}

body.accessibility-mode .accessibility-banner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.accessibility-banner button {
  background: var(--color-warning);
  color: #000;
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 0.85rem;
  min-height: 32px;
  font-weight: 700;
}

/* ==========================================================================
   Layout Containers
   ========================================================================== */
.container {
  width: 100%;
  max-width: 1180px;
  margin: 0 auto;
  padding: 0 16px;
  box-sizing: border-box;
}

.main-content {
  flex: 1;
  padding-bottom: 60px;
}

/* ==========================================================================
   Header & Navigation
   ========================================================================== */
.site-header {
  height: var(--header-height);
  background: var(--color-white);
  border-bottom: 1px solid var(--color-border);
  position: sticky;
  top: 0;
  z-index: 999;
  box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}

.header-inner {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: var(--color-text);
}

.logo-icon {
  width: 44px;
  height: 44px;
  background: var(--color-secondary);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-primary);
  flex-shrink: 0;
}

.logo-text h1 {
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--color-primary);
  line-height: 1.1;
  letter-spacing: -0.5px;
}

.logo-text span {
  font-size: 0.75rem;
  color: var(--color-muted);
  font-weight: 500;
  display: block;
}

.nav-group {
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-icon {
  display: none;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 6px;
  list-style: none;
}

.nav-link {
  color: var(--color-text);
  font-weight: 600;
  font-size: 0.95rem;
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  transition: all var(--transition);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.nav-link:hover {
  background: var(--color-secondary);
  color: var(--color-primary);
}

.badge-count {
  background: var(--color-primary);
  color: var(--color-white);
  font-size: 0.75rem;
  padding: 2px 7px;
  border-radius: 12px;
  font-weight: 700;
}

.header-controls {
  display: flex;
  align-items: center;
  gap: 8px;
}

.lang-selector-btn, .a11y-toggle-btn {
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--color-border);
  background: var(--color-white);
  color: var(--color-text);
  font-weight: 600;
  font-size: 0.9rem;
  gap: 6px;
}

.lang-selector-btn:hover, .a11y-toggle-btn:hover {
  border-color: var(--color-primary);
  background: var(--color-secondary);
  color: var(--color-primary);
}

.lang-dropdown-wrapper {
  position: relative;
}

.lang-menu {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 6px;
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-lg);
  display: none;
  flex-direction: column;
  min-width: 140px;
  z-index: 100;
  overflow: hidden;
}

.lang-menu.open {
  display: flex;
}

.lang-menu button {
  width: 100%;
  justify-content: flex-start;
  padding: 10px 14px;
  font-size: 0.9rem;
  font-weight: 500;
  border-radius: 0;
}

.lang-menu button:hover, .lang-menu button.active {
  background: var(--color-secondary);
  color: var(--color-primary);
  font-weight: 700;
}

.mobile-menu-btn {
  display: none;
}

/* ==========================================================================
   Progress Stepper
   ========================================================================== */
.stepper-section {
  background: var(--color-white);
  border-bottom: 1px solid var(--color-border);
  padding: 16px 0;
  margin-bottom: 24px;
}

.stepper-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  max-width: 860px;
  margin: 0 auto;
}

.stepper-nav::before {
  content: "";
  position: absolute;
  top: 18px;
  left: 24px;
  right: 24px;
  height: 3px;
  background: var(--color-border);
  z-index: 1;
}

.stepper-nav-progress {
  position: absolute;
  top: 18px;
  left: 24px;
  height: 3px;
  background: var(--color-primary);
  z-index: 2;
  transition: width var(--transition);
}

.step-item {
  position: relative;
  z-index: 3;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  background: var(--color-white);
  padding: 0 4px;
  cursor: pointer;
}

.step-circle {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--color-white);
  border: 2px solid var(--color-border);
  color: var(--color-muted);
  font-weight: 700;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all var(--transition);
}

.step-label {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--color-muted);
  white-space: nowrap;
}

.step-item.active .step-circle {
  border-color: var(--color-primary);
  background: var(--color-primary);
  color: var(--color-white);
  box-shadow: 0 0 0 4px var(--color-secondary);
}

.step-item.active .step-label {
  color: var(--color-primary);
  font-weight: 700;
}

.step-item.completed .step-circle {
  background: var(--color-primary);
  border-color: var(--color-primary);
  color: var(--color-white);
}

.step-item.completed .step-label {
  color: var(--color-text);
}

/* ==========================================================================
   Screen Containers & Transitions
   ========================================================================== */
.screen {
  display: none;
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 0.28s ease, transform 0.28s ease;
}

.screen.active {
  display: block;
  opacity: 1;
  transform: translateY(0);
}

/* Buttons & Components */
.btn {
  padding: 12px 24px;
  border-radius: var(--radius-sm);
  font-weight: 700;
  font-size: 1rem;
  gap: 8px;
  transition: all var(--transition);
}

.btn-primary {
  background: var(--color-primary);
  color: var(--color-white);
}

.btn-primary:hover {
  background: var(--color-primary-light);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(23,107,72,0.25);
}

.btn-secondary {
  background: var(--color-secondary);
  color: var(--color-primary);
}

.btn-secondary:hover {
  background: #d8ece0;
}

.btn-outline {
  border: 1px solid var(--color-border);
  background: var(--color-white);
  color: var(--color-text);
}

.btn-outline:hover {
  border-color: var(--color-primary);
  color: var(--color-primary);
  background: var(--color-secondary);
}

.btn-lg {
  padding: 16px 28px;
  font-size: 1.1rem;
  border-radius: 12px;
}

.btn-block {
  width: 100%;
}

.card {
  background: var(--color-white);
  border-radius: var(--radius);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow);
  padding: 24px;
  margin-bottom: 24px;
}

/* Status Badges */
.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.3px;
}

.status-available {
  background: #e6f7ee;
  color: var(--color-success);
  border: 1px solid #bcead0;
}

.status-rac {
  background: #fef8eb;
  color: #b57a12;
  border: 1px solid #f9e2b0;
}

.status-wl {
  background: #fdf2f2;
  color: var(--color-error);
  border: 1px solid #f8c8c8;
}

/* ==========================================================================
   SCREEN 1: Homepage & Search Card
   ========================================================================== */
.hero-section {
  position: relative;
  background: linear-gradient(145deg, #e4f4ea 0%, #f7faf8 55%, #e1efe6 100%);
  padding: 44px 0 60px;
  border-bottom: 1px solid var(--color-border);
  overflow: hidden;
}

.hero-bg-decoration {
  position: absolute;
  right: -50px;
  bottom: -40px;
  width: 480px;
  opacity: 0.12;
  pointer-events: none;
  color: var(--color-primary);
}

.hero-headline {
  text-align: center;
  max-width: 700px;
  margin: 0 auto 36px;
}

.hero-headline h2 {
  font-size: 2.3rem;
  font-weight: 800;
  color: var(--color-text);
  letter-spacing: -0.8px;
  line-height: 1.2;
  margin-bottom: 12px;
}

.hero-headline p {
  font-size: 1.15rem;
  color: var(--color-muted);
  font-weight: 500;
}

.search-card-wrapper {
  max-width: 900px;
  margin: 0 auto;
  position: relative;
  z-index: 5;
}

.search-card {
  background: var(--color-white);
  border-radius: var(--radius);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-lg);
  padding: 28px;
}

/* Journey Type Tabs */
.journey-tabs {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 24px;
  border-bottom: 1px solid var(--color-border);
  padding-bottom: 14px;
}

.tab-btn {
  padding: 8px 18px;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--color-muted);
  background: transparent;
  min-height: 38px;
}

.tab-btn.active {
  background: var(--color-primary);
  color: var(--color-white);
}

.tab-btn:not(.active):hover {
  background: var(--color-secondary);
  color: var(--color-primary);
}

.tab-badge-info {
  font-size: 0.72rem;
  background: #eef2ef;
  color: var(--color-muted);
  padding: 2px 6px;
  border-radius: 4px;
  margin-left: 6px;
}

/* Stations Grid */
.stations-row {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
  position: relative;
}

.station-input-group {
  position: relative;
}

.input-label {
  display: block;
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--color-muted);
  margin-bottom: 6px;
}

.input-with-icon {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 14px;
  color: var(--color-primary);
  pointer-events: none;
  display: flex;
  align-items: center;
}

.text-input {
  width: 100%;
  height: 52px;
  padding: 10px 14px 10px 44px;
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: #ffffff;
  color: var(--color-text);
  font-size: 1.05rem;
  font-weight: 600;
  transition: border-color var(--transition);
}

.text-input:focus {
  border-color: var(--color-primary);
  background: #ffffff;
}

.swap-btn-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 22px;
}

.swap-btn {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--color-secondary);
  border: 1.5px solid var(--color-border);
  color: var(--color-primary);
  transition: transform 0.3s ease, background 0.2s;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

.swap-btn:hover {
  background: #d4ebd9;
  transform: rotate(180deg);
}

/* Autocomplete Dropdown */
.autocomplete-dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin-top: 4px;
  background: var(--color-white);
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-lg);
  max-height: 280px;
  overflow-y: auto;
  z-index: 1000;
  display: none;
}

.autocomplete-dropdown.open {
  display: block;
}

.autocomplete-header {
  padding: 8px 12px;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--color-muted);
  background: #f6f8f6;
  border-bottom: 1px solid var(--color-border);
}

.autocomplete-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  cursor: pointer;
  border-bottom: 1px solid #f0f4f1;
  transition: background 0.15s;
}

.autocomplete-item:hover, .autocomplete-item.active {
  background: var(--color-secondary);
}

.station-details {
  display: flex;
  flex-direction: column;
}

.station-city {
  font-weight: 700;
  color: var(--color-text);
  font-size: 0.95rem;
}

.station-name {
  font-size: 0.8rem;
  color: var(--color-muted);
}

.station-code-badge {
  background: #eef5f0;
  color: var(--color-primary);
  font-weight: 800;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 0.85rem;
  letter-spacing: 0.5px;
}

/* Popular Station Chips */
.popular-chips {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 8px;
}

.chip-label {
  font-size: 0.72rem;
  color: var(--color-muted);
  font-weight: 600;
  margin-right: 4px;
}

.popular-chip {
  font-size: 0.75rem;
  padding: 3px 8px;
  border-radius: 12px;
  background: #edf5ef;
  color: var(--color-primary);
  border: 1px solid #d4e7d8;
  font-weight: 600;
  min-height: 26px;
}

.popular-chip:hover {
  background: var(--color-primary);
  color: var(--color-white);
}

/* Date & Passengers Row */
.details-row {
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  gap: 16px;
  margin-bottom: 20px;
}

.date-shortcuts {
  display: flex;
  gap: 6px;
  margin-top: 8px;
}

.shortcut-btn {
  font-size: 0.75rem;
  padding: 4px 10px;
  border-radius: 12px;
  background: #f0f4f1;
  border: 1px solid var(--color-border);
  color: var(--color-text);
  font-weight: 600;
  min-height: 28px;
}

.shortcut-btn:hover {
  background: var(--color-secondary);
  color: var(--color-primary);
  border-color: var(--color-primary);
}

/* Stepper Component */
.stepper-control {
  display: flex;
  align-items: center;
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: #ffffff;
  height: 52px;
  overflow: hidden;
}

.stepper-btn {
  width: 52px;
  height: 100%;
  background: #f6faf7;
  color: var(--color-primary);
  font-size: 1.3rem;
  font-weight: 700;
  transition: background 0.2s;
}

.stepper-btn:hover {
  background: var(--color-secondary);
}

.stepper-val {
  flex: 1;
  text-align: center;
  font-weight: 700;
  font-size: 1.15rem;
  color: var(--color-text);
}

/* Quota Selector */
.quota-row {
  margin-bottom: 24px;
}

.quota-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.quota-card {
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 12px 10px;
  text-align: center;
  cursor: pointer;
  background: #ffffff;
  transition: all var(--transition);
  position: relative;
}

.quota-card:hover {
  border-color: var(--color-primary);
  background: var(--color-secondary);
}

.quota-card.active {
  border-color: var(--color-primary);
  background: var(--color-secondary);
  box-shadow: 0 0 0 2px var(--color-primary);
}

.quota-card input[type="radio"] {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.quota-icon {
  font-size: 1.2rem;
  margin-bottom: 4px;
  display: block;
}

.quota-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--color-text);
  display: block;
}

.quota-desc {
  font-size: 0.72rem;
  color: var(--color-muted);
  display: block;
  margin-top: 2px;
}

.tatkal-badge {
  position: absolute;
  top: -8px;
  right: 6px;
  background: var(--color-warning);
  color: #000;
  font-size: 0.65rem;
  font-weight: 800;
  padding: 2px 6px;
  border-radius: 8px;
}

/* Help Section on Screen 1 — Mobile-First Inline Accordion */
.help-section {
  padding: 36px 0 24px;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}

.section-header {
  text-align: center;
  margin-bottom: 24px;
  padding: 0 8px;
}

.section-header h3 {
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--color-text);
  letter-spacing: -0.3px;
  line-height: 1.3;
}

.section-header p {
  color: var(--color-muted);
  font-size: 0.92rem;
  margin-top: 6px;
}

/* FAQ Accordion */
.faq-accordion {
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}

.faq-item {
  background: var(--color-white);
  border: 1.5px solid var(--color-border);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.25s ease;
  box-shadow: 0 1px 4px rgba(0,0,0,0.03);
  width: 100%;
  box-sizing: border-box;
}

.faq-item.open {
  border-color: var(--color-primary);
  box-shadow: 0 4px 16px rgba(23,107,72,0.1);
}

.faq-trigger {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 16px;
  background: none;
  border: none;
  cursor: pointer;
  text-align: left;
  gap: 10px;
  box-sizing: border-box;
}

.faq-trigger-left {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1;
  min-width: 0;
}

.faq-icon {
  font-size: 1.35rem;
  flex-shrink: 0;
}

.faq-question {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--color-text);
  line-height: 1.3;
  word-break: break-word;
}

.faq-trigger-right {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-shrink: 0;
}

.faq-read-more {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--color-primary);
  background: var(--color-secondary);
  padding: 4px 8px;
  border-radius: 6px;
  white-space: nowrap;
}

.faq-chevron {
  font-size: 0.75rem;
  color: var(--color-muted);
  transition: transform 0.3s ease;
  flex-shrink: 0;
}

.faq-item.open .faq-chevron {
  transform: rotate(180deg);
  color: var(--color-primary);
}

.faq-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  background: #fafdfb;
}

.faq-item.open .faq-body {
  max-height: 2500px;
  border-top: 1px solid #d8ebd9;
}

.faq-content-inner {
  padding: 16px;
  font-size: 0.88rem;
  line-height: 1.55;
  color: var(--color-text);
  box-sizing: border-box;
  width: 100%;
  overflow-x: hidden;
}

/* ==========================================================================
   SCREEN 2: Search Results
   ========================================================================== */
.results-header-bar {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 14px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  box-shadow: var(--shadow);
  width: 100%;
  box-sizing: border-box;
}

.results-summary-info {
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: 0;
  flex: 1;
}

.back-btn-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--color-secondary);
  color: var(--color-primary);
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.back-btn-circle:hover {
  background: #d8ece0;
}

.summary-route {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--color-text);
  line-height: 1.2;
}

.summary-meta {
  font-size: 0.8rem;
  color: var(--color-muted);
  margin-top: 2px;
  line-height: 1.3;
}

/* Filter Chips Bar (Phone Optimized - ZERO OVERLAPPING) */
.filter-bar {
  margin-bottom: 18px;
  width: 100%;
  max-width: 100%;
  overflow: hidden;
  box-sizing: border-box;
}

.filter-chips-scroll {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  overflow-x: auto !important;
  -webkit-overflow-scrolling: touch !important;
  padding: 4px 2px 8px 2px !important;
  scrollbar-width: none !important;
  width: 100% !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
}

.filter-chips-scroll::-webkit-scrollbar {
  display: none !important;
}

.filter-chip {
  flex-shrink: 0 !important;
  white-space: nowrap !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 8px 16px !important;
  border-radius: 20px !important;
  background: var(--color-white) !important;
  border: 1.5px solid var(--color-border) !important;
  font-size: 0.82rem !important;
  font-weight: 600 !important;
  line-height: 1.2 !important;
  color: var(--color-text) !important;
  min-height: 38px !important;
  box-sizing: border-box !important;
  cursor: pointer !important;
  user-select: none !important;
}

.filter-chip:hover {
  border-color: var(--color-primary) !important;
}

.filter-chip.active {
  background: var(--color-primary) !important;
  border-color: var(--color-primary) !important;
  color: var(--color-white) !important;
}

/* Tatkal Date Blocked Card */
.tatkal-date-blocked-card {
  background: var(--color-white);
  border: 2px dashed #f0b429;
  border-radius: var(--radius);
  padding: 24px 18px;
  text-align: center;
  box-shadow: 0 4px 16px rgba(217, 154, 37, 0.08);
  margin-bottom: 24px;
  width: 100%;
  box-sizing: border-box;
}

.tatkal-date-blocked-card h3 {
  font-size: 1.15rem;
  font-weight: 800;
  color: #a06306;
  margin-bottom: 8px;
}

.tatkal-date-blocked-card p {
  font-size: 0.88rem;
  color: var(--color-muted);
  line-height: 1.55;
  max-width: 460px;
  margin: 0 auto 16px;
}

.tatkal-blocked-actions {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 360px;
  margin: 0 auto;
}

/* Refund Tracker Modal Styles */
.refund-tracker-card {
  display: flex;
  flex-direction: column;
  gap: 14px;
  font-size: 0.88rem;
}

.refund-status-badge-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  background: #fef2f2;
  border: 1px solid #fecaca;
  border-radius: 8px;
  font-weight: 700;
}

.refund-breakdown-box {
  background: #f8faf9;
  border: 1px solid #e1ece4;
  border-radius: 10px;
  padding: 12px 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 0.85rem;
}

.refund-breakdown-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.refund-timeline {
  display: flex;
  flex-direction: column;
  gap: 14px;
  position: relative;
  padding-left: 28px;
  margin: 6px 0;
}

.refund-timeline::before {
  content: "";
  position: absolute;
  left: 9px;
  top: 8px;
  bottom: 8px;
  width: 2px;
  background: var(--color-primary);
}

.refund-step {
  position: relative;
}

.refund-step-dot {
  position: absolute;
  left: -28px;
  top: 1px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--color-primary);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: 800;
}

.refund-step-title {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-text);
}

.refund-step-desc {
  font-size: 0.78rem;
  color: var(--color-muted);
  margin-top: 2px;
  line-height: 1.4;
}

.demo-filter-toggle {
  font-size: 0.8rem;
  color: var(--color-muted);
  border: 1px dashed var(--color-border);
  padding: 6px 12px;
  border-radius: 8px;
  background: #fbfcfb;
}

.demo-filter-toggle:hover {
  color: var(--color-primary);
  border-color: var(--color-primary);
}

/* Train Cards */
.trains-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.train-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 24px;
  transition: transform var(--transition), box-shadow var(--transition);
  max-width: 100%;
  box-sizing: border-box;
}

.train-card:hover {
  box-shadow: var(--shadow-lg);
  border-color: #bce0c8;
}

.train-header-row {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f0f4f1;
}

.train-title-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  min-width: 0;
  flex: 1 1 auto;
}

.train-name-wrap {
  display: flex;
  align-items: center;
  min-width: 0;
}

.train-name {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--color-text);
  line-height: 1.25;
  word-break: break-word;
}

/* User requirement: keep express tag below the train number */
.train-tags-col {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 4px;
}

.train-number {
  background: #eef5f0;
  color: var(--color-primary);
  font-size: 0.8rem;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 6px;
  display: inline-block;
  width: fit-content;
}

.train-type-badge {
  font-size: 0.75rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 12px;
  background: #f0f3f1;
  color: var(--color-muted);
  display: inline-block;
  width: fit-content;
  white-space: nowrap;
}

.train-type-badge.superfast {
  background: #fff4e5;
  color: #ad6200;
}

.train-type-badge.tatkal {
  background: #fdf0f0;
  color: #c93b3b;
}

.running-days {
  display: flex;
  gap: 4px;
  align-items: center;
  flex-shrink: 0;
}

.day-badge {
  width: 22px;
  height: 22px;
  border-radius: 4px;
  font-size: 0.7rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f0f4f1;
  color: #a0b0a5;
  flex-shrink: 0;
  box-sizing: border-box;
}

.day-badge.active {
  background: var(--color-secondary);
  color: var(--color-primary);
}

/* Schedule Bar */
.train-schedule-grid {
  display: grid;
  grid-template-columns: 120px 1fr 120px;
  align-items: center;
  text-align: center;
  margin-bottom: 20px;
}

.schedule-point {
  text-align: left;
}

.schedule-point.dest {
  text-align: right;
}

.point-time {
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--color-text);
  line-height: 1.1;
}

.point-station {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--color-muted);
  margin-top: 2px;
}

.overnight-tag {
  font-size: 0.7rem;
  font-weight: 700;
  color: var(--color-warning);
  margin-left: 4px;
}

.route-indicator {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 16px;
}

.duration-text {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--color-muted);
  margin-bottom: 6px;
}

.route-line-visual {
  width: 100%;
  height: 3px;
  background: #dce7e0;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.route-line-visual::before, .route-line-visual::after {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-primary);
  position: absolute;
  top: -2.5px;
}

.route-line-visual::before { left: 0; }
.route-line-visual::after { right: 0; }

.route-train-icon {
  background: var(--color-white);
  padding: 0 6px;
  color: var(--color-primary);
}

/* Train Card Classes Grid */
.train-classes-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 10px;
  margin-bottom: 16px;
}

.class-mini-card {
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 10px;
  cursor: pointer;
  background: #fbfcfb;
  transition: all var(--transition);
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.class-mini-card:hover {
  border-color: var(--color-primary);
  background: var(--color-secondary);
}

.class-mini-card.selected {
  border-color: var(--color-primary);
  background: #eef8f2;
  box-shadow: 0 0 0 2px var(--color-primary);
}

.class-mini-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.class-mini-code {
  font-weight: 800;
  font-size: 0.95rem;
  color: var(--color-text);
}

.class-mini-fare {
  font-weight: 800;
  font-size: 1.05rem;
  color: var(--color-primary);
}

.class-mini-status {
  font-size: 0.75rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 4px;
}

.train-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 14px;
  border-top: 1px solid #f0f4f1;
}

.train-features {
  font-size: 0.8rem;
  color: var(--color-muted);
  display: flex;
  gap: 14px;
}

/* No Trains State */
.no-trains-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 48px 24px;
  text-align: center;
  box-shadow: var(--shadow);
}

.no-trains-icon {
  width: 90px;
  height: 90px;
  background: #fceeee;
  color: var(--color-error);
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.no-trains-card h3 {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--color-text);
  margin-bottom: 8px;
}

.no-trains-card p {
  color: var(--color-muted);
  max-width: 480px;
  margin: 0 auto 24px;
}

.alternate-dates-list {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.alternate-date-chip {
  padding: 8px 16px;
  border-radius: 20px;
  border: 1px solid var(--color-border);
  background: var(--color-secondary);
  color: var(--color-primary);
  font-weight: 700;
  font-size: 0.85rem;
}

.alternate-date-chip:hover {
  background: var(--color-primary);
  color: var(--color-white);
}

/* ==========================================================================
   SCREEN 3: Class & Seat Selection
   ========================================================================== */
.selection-header-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 20px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow);
}

.tatkal-status-banner {
  background: #fff9ea;
  border: 1.5px solid var(--color-warning);
  border-radius: var(--radius);
  padding: 16px 20px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.tatkal-banner-left {
  display: flex;
  align-items: center;
  gap: 14px;
}

.tatkal-clock-icon {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #ffecb5;
  color: #a06300;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  flex-shrink: 0;
}

.tatkal-banner-info h4 {
  font-size: 1rem;
  font-weight: 800;
  color: #8c5500;
}

.tatkal-banner-info p {
  font-size: 0.85rem;
  color: #6d4a13;
  margin-top: 2px;
}

.tatkal-timer-badge {
  background: #8c5500;
  color: #fff;
  font-weight: 800;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 0.9rem;
  letter-spacing: 0.5px;
  white-space: nowrap;
}

.tatkal-demo-btns {
  display: flex;
  gap: 6px;
  margin-top: 8px;
}

.tatkal-demo-btn {
  font-size: 0.72rem;
  padding: 2px 8px;
  border-radius: 6px;
  background: #fae7ba;
  color: #724200;
  border: 1px solid #e5c37e;
  min-height: 24px;
}

/* Detailed Class Cards */
.classes-detail-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.class-card {
  background: var(--color-white);
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 22px;
  display: flex;
  flex-direction: column;
  transition: all var(--transition);
  position: relative;
}

.class-card:hover {
  box-shadow: var(--shadow-lg);
  border-color: var(--color-primary);
}

.class-card-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 12px;
}

.class-card-name h4 {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--color-text);
  line-height: 1.2;
}

.class-code-tag {
  background: var(--color-secondary);
  color: var(--color-primary);
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 8px;
  font-size: 0.9rem;
}

.berth-visual-box {
  background: #f6faf7;
  border: 1px solid #dcebe0;
  border-radius: var(--radius-sm);
  padding: 12px;
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.berth-svg-icon {
  color: var(--color-primary);
  flex-shrink: 0;
}

.class-description {
  font-size: 0.88rem;
  color: var(--color-muted);
  line-height: 1.45;
  margin-bottom: 16px;
  flex: 1;
}

.class-fare-box {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  padding: 12px 0;
  border-top: 1px solid #f0f4f1;
  border-bottom: 1px solid #f0f4f1;
  margin-bottom: 14px;
}

.class-fare-label {
  font-size: 0.8rem;
  color: var(--color-muted);
  font-weight: 600;
}

.class-fare-amount {
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--color-text);
}

.class-availability-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.class-note-alert {
  font-size: 0.78rem;
  padding: 8px 12px;
  border-radius: 8px;
  margin-bottom: 16px;
  line-height: 1.4;
}

.class-note-alert.wl {
  background: #fdf1f1;
  color: var(--color-error);
  border: 1px solid #facfcf;
}

.class-note-alert.rac {
  background: #fef9ec;
  color: #ad6d00;
  border: 1px solid #f7dfa7;
}

.class-note-alert.avl {
  background: #edf8f1;
  color: var(--color-success);
  border: 1px solid #c8ecd4;
}

/* ==========================================================================
   SCREEN 4: Passenger Details
   ========================================================================== */
.booking-summary-accordion {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  margin-bottom: 24px;
  box-shadow: var(--shadow);
  overflow: hidden;
}

.accordion-header {
  padding: 16px 20px;
  background: #f6faf7;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-weight: 700;
  color: var(--color-text);
}

.accordion-header:hover {
  background: #eef6f1;
}

.accordion-content {
  padding: 20px;
  border-top: 1px solid var(--color-border);
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.summary-stat-label {
  font-size: 0.75rem;
  color: var(--color-muted);
  font-weight: 700;
  text-transform: uppercase;
}

.summary-stat-value {
  font-size: 1rem;
  font-weight: 700;
  color: var(--color-text);
  margin-top: 2px;
}

/* Passenger Forms List */
.passenger-forms-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 24px;
}

.passenger-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: var(--shadow);
}

.passenger-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 18px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f0f4f1;
}

.passenger-badge-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 800;
  font-size: 1.1rem;
  color: var(--color-text);
}

.passenger-num-pill {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--color-primary);
  color: var(--color-white);
  font-size: 0.85rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.passenger-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1.5fr 1.5fr;
  gap: 16px;
  margin-bottom: 16px;
}

.form-group {
  position: relative;
  display: flex;
  flex-direction: column;
}

.form-group label {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--color-muted);
  margin-bottom: 6px;
}

.form-input-wrap {
  position: relative;
  display: flex;
  align-items: center;
}

.form-control {
  width: 100%;
  height: 48px;
  padding: 8px 14px;
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: #ffffff;
  color: var(--color-text);
  font-size: 0.95rem;
  font-weight: 600;
  transition: border-color var(--transition);
}

.form-control:focus {
  border-color: var(--color-primary);
}

.form-control.is-invalid {
  border-color: var(--color-error);
  background-color: #fdf7f7;
}

.form-control.is-valid {
  border-color: var(--color-success);
  background-color: #f6fbf7;
}

.input-valid-icon {
  position: absolute;
  right: 12px;
  color: var(--color-success);
  pointer-events: none;
  display: none;
}

.form-control.is-valid ~ .input-valid-icon {
  display: block;
}

.error-text {
  color: var(--color-error);
  font-size: 0.75rem;
  font-weight: 600;
  margin-top: 4px;
  display: none;
}

.form-control.is-invalid ~ .error-text {
  display: block;
}

/* Gender Selection Radio Pills */
.gender-pills-group {
  display: flex;
  gap: 6px;
  height: 48px;
}

.gender-pill {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-weight: 600;
  font-size: 0.85rem;
  transition: all 0.2s;
  background: #fff;
}

.gender-pill input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.gender-pill:hover {
  background: #f7faf8;
}

.gender-pill.active {
  border-color: var(--color-primary);
  background: var(--color-secondary);
  color: var(--color-primary);
  font-weight: 700;
}

/* Senior Citizen Checkbox */
.senior-check-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  background: #f8faf8;
  border-radius: var(--radius-sm);
  border: 1px dashed var(--color-border);
  cursor: default;
  pointer-events: none;
  user-select: none;
}

.senior-check-row input[type="checkbox"] {
  width: 18px;
  height: 18px;
  accent-color: var(--color-primary);
  cursor: default;
  pointer-events: none;
}

.senior-check-label {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--color-text);
  cursor: default;
}

.senior-discount-badge {
  font-size: 0.72rem;
  background: #e5f6eb;
  color: var(--color-success);
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  margin-left: auto;
}

/* Contact Details Card */
.contact-details-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: var(--shadow);
  margin-bottom: 24px;
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 12px;
}

.mobile-input-wrap {
  display: flex;
  align-items: center;
}

.country-code-pill {
  height: 48px;
  padding: 0 14px;
  background: #eef3ef;
  border: 1.5px solid var(--color-border);
  border-right: none;
  border-top-left-radius: var(--radius-sm);
  border-bottom-left-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--color-text);
}

.mobile-input-wrap .form-control {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.contact-notice-box {
  font-size: 0.8rem;
  color: var(--color-muted);
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 8px;
}

/* ==========================================================================
   SCREEN 5: Payment
   ========================================================================== */
.payment-layout {
  display: grid;
  grid-template-columns: 1.6fr 1fr;
  gap: 24px;
  align-items: flex-start;
}

.payment-methods-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 24px;
}

.payment-tabs-nav {
  display: flex;
  gap: 8px;
  border-bottom: 1.5px solid var(--color-border);
  margin-bottom: 24px;
  padding-bottom: 12px;
}

.pay-tab-btn {
  padding: 8px 16px;
  border-radius: var(--radius-sm);
  font-weight: 700;
  font-size: 0.9rem;
  color: var(--color-muted);
  background: #f7faf8;
  border: 1px solid var(--color-border);
}

.pay-tab-btn.active {
  background: var(--color-primary);
  border-color: var(--color-primary);
  color: var(--color-white);
}

.pay-tab-content {
  display: none;
}

.pay-tab-content.active {
  display: block;
}

/* UPI Styles */
.upi-apps-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 24px;
}

.upi-app-btn {
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 14px 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  background: #fff;
  transition: all var(--transition);
}

.upi-app-btn:hover, .upi-app-btn.active {
  border-color: var(--color-primary);
  background: var(--color-secondary);
  box-shadow: 0 0 0 2px var(--color-primary);
}

.upi-icon-badge {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: 800;
}

.upi-verify-row {
  display: flex;
  gap: 10px;
  margin-bottom: 16px;
}

/* Card Styles */
.card-form-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 14px;
  margin-bottom: 16px;
}

.card-number-row {
  grid-column: 1 / -1;
}

.card-security-note {
  font-size: 0.78rem;
  color: var(--color-muted);
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 10px;
}

/* Net Banking Grid */
.banks-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  margin-bottom: 16px;
}

.bank-item-btn {
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 12px 8px;
  text-align: center;
  background: #fff;
  font-size: 0.85rem;
  font-weight: 700;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}

.bank-item-btn:hover, .bank-item-btn.active {
  border-color: var(--color-primary);
  background: var(--color-secondary);
  color: var(--color-primary);
}

.bank-abbr {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--color-primary);
}

/* Wallets Grid */
.wallets-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.wallet-btn {
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  background: #fff;
  font-weight: 700;
}

.wallet-btn:hover, .wallet-btn.active {
  border-color: var(--color-primary);
  background: var(--color-secondary);
}

/* Fare Breakdown Card (Right Column) */
.fare-breakdown-card {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 24px;
  position: sticky;
  top: 90px;
}

.fare-breakdown-card h3 {
  font-size: 1.25rem;
  font-weight: 800;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f0f4f1;
}

.fare-line-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
  font-size: 0.92rem;
}

.fare-line-item.total {
  margin-top: 16px;
  padding-top: 14px;
  border-top: 2px dashed var(--color-border);
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--color-primary);
}

.simulated-note-badge {
  background: #f1f7f3;
  color: var(--color-muted);
  font-size: 0.75rem;
  padding: 6px 10px;
  border-radius: 6px;
  text-align: center;
  margin: 16px 0;
  border: 1px solid #d8ebd9;
}

.demo-failure-checkbox-wrap {
  background: #fff8f8;
  border: 1px dashed #f5c4c4;
  border-radius: var(--radius-sm);
  padding: 12px;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.demo-failure-checkbox-wrap input {
  accent-color: var(--color-error);
  cursor: pointer;
  width: 18px;
  height: 18px;
}

.demo-failure-checkbox-wrap label {
  font-size: 0.8rem;
  color: #a82e2e;
  font-weight: 600;
  cursor: pointer;
}

/* Payment Processing Overlay */
.processing-overlay {
  position: fixed;
  inset: 0;
  background: rgba(23, 107, 72, 0.45);
  backdrop-filter: blur(4px);
  z-index: 2000;
  display: none;
  align-items: center;
  justify-content: center;
}

.processing-card {
  background: var(--color-white);
  border-radius: var(--radius);
  padding: 36px 40px;
  max-width: 440px;
  width: 90%;
  text-align: center;
  box-shadow: 0 16px 48px rgba(0,0,0,0.2);
}

.processing-spinner {
  width: 64px;
  height: 64px;
  border: 5px solid #d4ebda;
  border-top-color: var(--color-primary);
  border-radius: 50%;
  animation: spin 0.9s linear infinite;
  margin: 0 auto 20px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.processing-card h3 {
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--color-text);
  margin-bottom: 8px;
}

.processing-card p {
  color: var(--color-muted);
  font-size: 0.92rem;
}

/* Payment Failure Alert within Screen 5 */
.payment-failure-box {
  background: #fff5f5;
  border: 1.5px solid #f8b4b4;
  border-radius: var(--radius);
  padding: 24px;
  margin-bottom: 24px;
  display: none;
}

.failure-header {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 12px;
}

.failure-icon-wrap {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #fde2e2;
  color: var(--color-error);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  flex-shrink: 0;
}

.failure-header h3 {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--color-error);
}

.failure-details {
  background: #fff;
  border: 1px solid #fad0d0;
  border-radius: var(--radius-sm);
  padding: 12px 16px;
  margin-bottom: 16px;
  font-size: 0.88rem;
  color: var(--color-text);
}

.failure-actions {
  display: flex;
  gap: 12px;
}

/* ==========================================================================
   SCREEN 6: Booking Confirmation & Digital Ticket
   ========================================================================== */
.success-banner {
  text-align: center;
  padding: 32px 0 20px;
}

.success-animated-icon {
  width: 76px;
  height: 76px;
  background: #e5f6eb;
  border: 3px solid var(--color-success);
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 2.2rem;
  color: var(--color-success);
  margin-bottom: 16px;
  animation: bounceIn 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@keyframes bounceIn {
  0% { transform: scale(0.3); opacity: 0; }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); opacity: 1; }
}

.success-banner h2 {
  font-size: 2rem;
  font-weight: 800;
  color: var(--color-text);
  letter-spacing: -0.5px;
}

.success-banner p {
  color: var(--color-muted);
  font-size: 1.05rem;
  margin-top: 6px;
}

/* Digital Ticket Container */
.ticket-wrapper {
  max-width: 820px;
  margin: 0 auto 30px;
}

.ticket-card {
  background: var(--color-white);
  border: 2px solid var(--color-primary);
  border-radius: var(--radius);
  box-shadow: var(--shadow-lg);
  overflow: hidden;
  position: relative;
}

.ticket-header-top {
  background: var(--color-primary);
  color: var(--color-white);
  padding: 14px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px 12px;
}

.ticket-brand-left {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1 1 auto;
  min-width: 0;
}

.ticket-brand-left h3 {
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: 0.3px;
  line-height: 1.25;
  word-break: break-word;
}

.simulated-badge-red {
  background: #ff4747;
  color: #fff;
  font-size: 0.68rem;
  font-weight: 800;
  padding: 4px 8px;
  border-radius: 4px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  border: 1px solid #ffffff;
  white-space: normal;
  text-align: center;
  line-height: 1.25;
}

.ticket-pnr-banner {
  background: var(--color-secondary);
  padding: 12px 20px;
  border-bottom: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px 16px;
}

.pnr-box-left {
  display: flex;
  align-items: baseline;
  gap: 10px;
}

.pnr-label {
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--color-muted);
}

.pnr-number {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: 2px;
  color: var(--color-primary);
  font-family: monospace;
}

.pnr-meta-right {
  font-size: 0.85rem;
  color: var(--color-text);
  text-align: right;
  line-height: 1.35;
}

.pnr-meta-txn {
  color: var(--color-muted);
  font-size: 0.78rem;
}

.copy-pnr-btn {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--color-primary);
  background: #fff;
  border: 1px solid var(--color-border);
  padding: 4px 12px;
  border-radius: 6px;
  min-height: 32px;
}

.copy-pnr-btn:hover {
  background: var(--color-secondary);
}

.ticket-body {
  padding: 24px;
}

.ticket-journey-grid {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 1px dashed var(--color-border);
  margin-bottom: 20px;
}

.journey-node.dest {
  text-align: right;
}

.node-time {
  font-size: 1.7rem;
  font-weight: 800;
  color: var(--color-text);
}

.node-stn-code {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--color-primary);
}

.node-stn-name {
  font-size: 0.85rem;
  color: var(--color-muted);
}

.journey-mid-train {
  text-align: center;
  padding: 0 16px;
}

.train-title-big {
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--color-text);
}

.train-meta-pill {
  font-size: 0.78rem;
  background: #f0f4f1;
  color: var(--color-muted);
  padding: 3px 8px;
  border-radius: 6px;
  display: inline-block;
  margin-top: 4px;
}

/* Passenger Table on Ticket */
.ticket-passengers-table-wrap {
  margin-bottom: 24px;
  overflow-x: auto;
}

.ticket-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.ticket-table th {
  background: #f7faf8;
  padding: 8px 10px;
  font-weight: 700;
  font-size: 0.82rem;
  color: var(--color-muted);
  text-align: left;
  border-bottom: 1.5px solid var(--color-border);
  word-break: break-word;
  line-height: 1.2;
}

.ticket-table td {
  padding: 9px 10px;
  border-bottom: 1px solid #f0f4f1;
  color: var(--color-text);
  font-weight: 600;
  font-size: 0.84rem;
  word-break: break-word;
  line-height: 1.25;
}

.ticket-security-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 20px;
  border-top: 1.5px solid var(--color-border);
}

.qr-code-placeholder {
  display: flex;
  align-items: center;
  gap: 16px;
}

.qr-svg {
  width: 76px;
  height: 76px;
  background: #f7faf8;
  border: 1px solid var(--color-border);
  padding: 4px;
  border-radius: 8px;
}

.qr-caption {
  font-size: 0.75rem;
  color: var(--color-muted);
  max-width: 220px;
  line-height: 1.4;
}

.ticket-total-fare {
  text-align: right;
}

.ticket-fare-label {
  font-size: 0.8rem;
  color: var(--color-muted);
  font-weight: 700;
  text-transform: uppercase;
}

.ticket-fare-val {
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--color-primary);
}

/* Ticket Actions Toolbar */
.ticket-actions-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}

.hackathon-disclaimer {
  background: #f4faf6;
  border: 1px solid #cce8d4;
  border-radius: var(--radius-sm);
  padding: 14px 20px;
  text-align: center;
  font-size: 0.85rem;
  color: var(--color-muted);
  max-width: 820px;
  margin: 0 auto;
}

/* ==========================================================================
   Modals & Drawers
   ========================================================================== */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 30, 20, 0.6);
  backdrop-filter: blur(4px);
  z-index: 2100;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 16px;
}

.modal-overlay.open {
  display: flex;
}

.modal-card {
  background: var(--color-white);
  border-radius: var(--radius);
  max-width: 640px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0,0,0,0.25);
  animation: modalPop 0.25s ease-out;
}

@keyframes modalPop {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}

.modal-header {
  padding: 20px 24px;
  border-bottom: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-header h3 {
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--color-text);
}

.modal-close-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  font-size: 1.2rem;
  color: var(--color-muted);
}

.modal-close-btn:hover {
  background: #f0f4f1;
  color: var(--color-text);
}

.modal-body {
  padding: 24px;
}

.modal-footer {
  padding: 16px 24px;
  border-top: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 12px;
  background: #f9fbf9;
}

/* Help Modal Tabs */
.help-modal-tabs {
  display: flex;
  gap: 6px;
  border-bottom: 1.5px solid var(--color-border);
  margin-bottom: 20px;
  overflow-x: auto;
}

.help-modal-tab-btn {
  padding: 8px 14px;
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--color-muted);
  border-radius: 6px 6px 0 0;
  border-bottom: 2px solid transparent;
}

.help-modal-tab-btn.active {
  color: var(--color-primary);
  border-bottom-color: var(--color-primary);
  background: #eef7f1;
}

/* My Bookings Drawer */
.bookings-drawer {
  position: fixed;
  top: 0;
  right: -480px;
  width: 100%;
  max-width: 460px;
  height: 100vh;
  background: var(--color-white);
  box-shadow: -8px 0 32px rgba(0,0,0,0.15);
  z-index: 2200;
  transition: right 0.3s ease;
  display: flex;
  flex-direction: column;
}

.bookings-drawer.open {
  right: 0;
}

.drawer-header {
  padding: 20px 24px;
  border-bottom: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.drawer-content {
  flex: 1;
  overflow-y: auto;
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.empty-bookings-box {
  text-align: center;
  padding: 48px 16px;
  color: var(--color-muted);
}

.saved-booking-item {
  border: 1.5px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: 16px;
  background: #fcfdfc;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.saved-booking-item.cancelled {
  opacity: 0.6;
  border-style: dashed;
}

/* Toast Notifications */
.toast-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 3000;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.toast {
  background: #172d1f;
  color: #fff;
  padding: 12px 20px;
  border-radius: var(--radius-sm);
  font-size: 0.9rem;
  font-weight: 600;
  box-shadow: 0 6px 20px rgba(0,0,0,0.25);
  display: flex;
  align-items: center;
  gap: 10px;
  animation: slideToast 0.25s ease-out;
}

@keyframes slideToast {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

/* ==========================================================================
   Print Styles
   ========================================================================== */
@media print {
  body > *:not(#ticket-section) { display: none; }
  #ticket-section { display: block; }
  .no-print { display: none; }

  body {
    background: #ffffff !important;
    color: #000000 !important;
  }
  body > .main-content {
    display: block !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  .main-content > *:not([data-screen="6"]) {
    display: none !important;
  }
  .screen:not([data-screen="6"]) {
    display: none !important;
  }
  [data-screen="6"] {
    display: block !important;
    padding: 0 !important;
  }
  .success-banner {
    display: none !important;
  }
  #ticket-section {
    display: block !important;
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
  }
  .ticket-card {
    border: 2px solid #000000 !important;
    box-shadow: none !important;
    page-break-inside: avoid;
  }
}

/* ==========================================================================
   Responsive Breakpoints
   ========================================================================== */
@media (max-width: 900px) {
  .stations-row {
    grid-template-columns: 1fr;
  }
  
  .swap-btn-container {
    margin: -6px 0;
  }
  
  .details-row {
    grid-template-columns: 1fr;
  }
  
  .quota-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .help-grid {
    grid-template-columns: 1fr;
  }
  
  .payment-layout {
    grid-template-columns: 1fr;
  }
  
  .passenger-grid {
    grid-template-columns: 1fr;
  }
  
  .card-form-grid {
    grid-template-columns: 1fr;
  }
  
  .upi-apps-grid, .banks-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .accordion-content {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  html, body {
    overflow-x: hidden !important;
    max-width: 100vw !important;
    width: 100% !important;
    position: relative !important;
  }

  .container {
    padding: 0 12px !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
  }

  .site-header {
    height: auto !important;
    min-height: 56px !important;
    padding: 6px 0 !important;
  }

  .header-inner {
    gap: 6px !important;
    padding: 0 2px !important;
    width: 100% !important;
    box-sizing: border-box !important;
    justify-content: space-between !important;
  }

  .brand-logo {
    gap: 6px !important;
    flex-shrink: 0 !important;
  }

  .logo-icon {
    width: 32px !important;
    height: 32px !important;
    border-radius: 8px !important;
  }

  .logo-icon svg {
    width: 18px !important;
    height: 18px !important;
  }

  .logo-text h1 {
    font-size: 1.12rem !important;
    line-height: 1.1 !important;
  }

  .logo-text span {
    display: none !important;
  }

  .nav-group {
    gap: 4px !important;
    flex-shrink: 0 !important;
  }

  .nav-links {
    gap: 3px !important;
  }

  .nav-icon {
    display: inline-flex !important;
  }

  .nav-text {
    display: none !important;
  }

  .nav-link {
    padding: 6px 6px !important;
    min-width: 36px !important;
    min-height: 36px !important;
    font-size: 0.85rem !important;
  }

  .badge-count {
    padding: 1px 5px !important;
    font-size: 0.65rem !important;
    margin-left: 2px !important;
  }

  .header-controls {
    gap: 4px !important;
    flex-shrink: 0 !important;
    margin-left: 2px !important;
  }

  .lang-selector-btn {
    padding: 6px 8px !important;
    min-height: 36px !important;
    min-width: 44px !important;
    font-size: 0.82rem !important;
    white-space: nowrap !important;
    gap: 4px !important;
    flex-shrink: 0 !important;
  }

  .lang-dropdown-wrapper {
    position: relative !important;
    flex-shrink: 0 !important;
  }

  .lang-menu {
    right: 0 !important;
    left: auto !important;
    max-width: calc(100vw - 20px) !important;
    z-index: 1000 !important;
  }

  .search-card {
    padding: 18px 14px !important;
  }
  
  .hero-headline h2 {
    font-size: 1.7rem;
  }

  /* Train card phone styling */
  .train-card {
    padding: 16px 12px !important;
    border-radius: var(--radius-sm);
  }

  .train-header-row {
    gap: 8px;
    margin-bottom: 12px;
    padding-bottom: 10px;
  }

  .train-name {
    font-size: 1.05rem;
  }

  .train-tags-col {
    gap: 3px;
  }

  .train-number {
    font-size: 0.75rem;
    padding: 2px 6px;
  }

  .train-type-badge {
    font-size: 0.7rem;
    padding: 2px 6px;
  }

  .running-days {
    gap: 2.5px;
  }

  .day-badge {
    width: 20px;
    height: 20px;
    font-size: 0.62rem;
  }

  .train-classes-row {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 8px;
    margin-bottom: 14px;
  }

  .class-mini-card {
    padding: 8px;
  }

  .class-mini-code {
    font-size: 0.88rem;
  }

  .class-mini-fare {
    font-size: 0.92rem;
  }

  .status-pill {
    font-size: 0.7rem;
    padding: 2px 6px;
  }

  .train-card-footer {
    flex-direction: column;
    align-items: stretch;
    gap: 10px;
    padding-top: 12px;
  }

  .train-features {
    justify-content: center;
    gap: 12px;
    font-size: 0.75rem;
    flex-wrap: wrap;
  }

  .btn-select-train {
    width: 100%;
    min-height: 42px;
  }

  .results-header-bar {
    padding: 10px 12px;
  }
  
  .train-schedule-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  
  .schedule-point, .schedule-point.dest {
    text-align: center;
  }
  
  .step-label {
    display: none;
  }
  
  .ticket-journey-grid {
    grid-template-columns: 1fr;
    gap: 16px;
    text-align: center;
  }
  
  .journey-node.dest {
    text-align: center;
  }
  
  .contact-grid {
    grid-template-columns: 1fr;
  }

  /* Ticket Card Mobile Fitting: Zero text cut-off, multiple line rearrangement & font scaling */
  .ticket-wrapper {
    margin: 0 auto 16px !important;
    max-width: 100% !important;
  }

  .ticket-card {
    border-radius: var(--radius-sm) !important;
    overflow: hidden !important;
    word-break: break-word !important;
  }

  .ticket-header-top {
    padding: 10px 12px !important;
    gap: 6px 10px !important;
    flex-direction: column !important;
    align-items: flex-start !important;
  }

  .ticket-brand-left h3 {
    font-size: 0.88rem !important;
    line-height: 1.25 !important;
    word-break: break-word !important;
  }

  .simulated-badge-red {
    font-size: 0.58rem !important;
    padding: 2px 6px !important;
    line-height: 1.2 !important;
    white-space: normal !important;
    align-self: flex-start !important;
    text-align: left !important;
  }

  .ticket-pnr-banner {
    padding: 10px 12px !important;
    gap: 8px !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
  }

  .pnr-box-left {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    width: 100% !important;
    gap: 6px !important;
  }

  .pnr-label {
    font-size: 0.72rem !important;
  }

  .pnr-number {
    font-size: 1.15rem !important;
    letter-spacing: 1px !important;
  }

  .pnr-meta-right {
    font-size: 0.72rem !important;
    text-align: left !important;
    line-height: 1.35 !important;
    width: 100% !important;
    border-top: 1px dashed rgba(23,107,72,0.18) !important;
    padding-top: 6px !important;
    margin-top: 2px !important;
  }

  .pnr-meta-txn {
    font-size: 0.68rem !important;
  }

  .ticket-body {
    padding: 14px 10px !important;
  }

  .ticket-journey-grid {
    grid-template-columns: 1fr !important;
    gap: 10px !important;
    text-align: center !important;
    padding-bottom: 12px !important;
    margin-bottom: 12px !important;
  }

  .node-time {
    font-size: 1.35rem !important;
  }

  .node-stn-code {
    font-size: 1.05rem !important;
  }

  .node-stn-name {
    font-size: 0.78rem !important;
    word-break: break-word !important;
  }

  .train-title-big {
    font-size: 0.92rem !important;
    word-break: break-word !important;
  }

  .train-meta-pill {
    font-size: 0.72rem !important;
    white-space: normal !important;
    word-break: break-word !important;
    max-width: 100% !important;
  }

  /* Compact Ticket Table on Mobile */
  .ticket-passengers-table-wrap {
    margin-bottom: 16px !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
  }

  .ticket-table {
    width: 100% !important;
    min-width: 280px !important;
    font-size: 0.74rem !important;
  }

  .ticket-table th {
    padding: 6px 3px !important;
    font-size: 0.68rem !important;
    white-space: normal !important;
    word-break: break-word !important;
    line-height: 1.15 !important;
  }

  .ticket-table td {
    padding: 7px 3px !important;
    font-size: 0.72rem !important;
    white-space: normal !important;
    word-break: break-word !important;
    line-height: 1.2 !important;
  }

  .ticket-table td .status-pill {
    font-size: 0.62rem !important;
    padding: 1px 4px !important;
  }

  /* Security Footer on Mobile */
  .ticket-security-footer {
    flex-direction: column !important;
    align-items: stretch !important;
    gap: 12px !important;
    padding-top: 12px !important;
  }

  .qr-code-placeholder {
    width: 100% !important;
    gap: 10px !important;
  }

  .qr-svg {
    width: 52px !important;
    height: 52px !important;
    flex-shrink: 0 !important;
  }

  .qr-caption {
    font-size: 0.68rem !important;
    max-width: 100% !important;
    line-height: 1.3 !important;
  }

  .ticket-total-fare {
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    text-align: left !important;
    border-top: 1px dashed var(--color-border) !important;
    padding-top: 8px !important;
  }

  .ticket-fare-val {
    font-size: 1.35rem !important;
  }

  /* Accessible Buttons & Controls Across All Screens on Mobile */
  .selection-header-card {
    flex-wrap: wrap !important;
    gap: 10px !important;
    padding: 12px 14px !important;
  }

  .classes-detail-grid {
    grid-template-columns: 1fr !important;
  }

  .btn-select-class {
    width: 100% !important;
    min-height: 44px !important;
  }

  .tatkal-status-banner {
    flex-direction: column !important;
    align-items: stretch !important;
    gap: 12px !important;
  }

  .tatkal-demo-btns {
    flex-wrap: wrap !important;
    gap: 6px !important;
  }

  .passenger-submit-row {
    width: 100% !important;
    display: flex !important;
    justify-content: stretch !important;
  }

  #btn-continue-to-payment {
    width: 100% !important;
    min-width: 100% !important;
    min-height: 48px !important;
  }

  .payment-tabs-nav {
    flex-wrap: wrap !important;
    gap: 8px !important;
    border-bottom: none !important;
  }

  .pay-tab-btn {
    flex: 1 1 calc(50% - 8px) !important;
    text-align: center !important;
    padding: 10px 8px !important;
    min-height: 44px !important;
    font-size: 0.85rem !important;
  }

  .failure-actions {
    flex-direction: column !important;
    width: 100% !important;
    gap: 10px !important;
  }

  .failure-actions .btn {
    width: 100% !important;
    min-height: 44px !important;
  }

  .ticket-actions-bar {
    flex-direction: column !important;
    width: 100% !important;
    gap: 10px !important;
  }

  .ticket-actions-bar .btn {
    width: 100% !important;
    min-height: 46px !important;
    justify-content: center !important;
  }
}

@media (max-width: 360px) {
  .running-days {
    gap: 1.5px;
  }
  .day-badge {
    width: 18px;
    height: 18px;
    font-size: 0.58rem;
  }
  .ticket-brand-left h3 {
    font-size: 0.85rem;
  }
  .pnr-number {
    font-size: 1.05rem !important;
    letter-spacing: 0.5px !important;
  }
  .pnr-meta-right {
    font-size: 0.68rem !important;
  }
}

/* ==========================================================================
   Sarvam AI Deep Context Translation System Styles
   ========================================================================== */

/* Navbar & Header Controls */
.lang-menu-heading {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--color-muted);
  padding: 8px 12px 4px 12px;
}

.lang-menu-divider {
  height: 1px;
  background-color: var(--color-border);
  margin: 6px 0;
}

.sarvam-menu-item {
  display: flex !important;
  align-items: center;
  gap: 8px;
  color: #155724 !important;
  font-weight: 600 !important;
  background: rgba(23, 107, 72, 0.06) !important;
  border-radius: 6px;
  margin: 4px;
  padding: 8px 12px;
  transition: all var(--transition);
}

.sarvam-menu-item:hover {
  background: rgba(23, 107, 72, 0.14) !important;
}

.sarvam-nav-btn {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  background: linear-gradient(135deg, #176B48 0%, #0d4a31 100%);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 8px 14px;
  border-radius: 20px;
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  transition: all var(--transition);
  box-shadow: 0 2px 8px rgba(23, 107, 72, 0.25);
  white-space: nowrap;
}

.sarvam-nav-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(23, 107, 72, 0.35);
  background: linear-gradient(135deg, #1a7d55 0%, #125e3e 100%);
}

.sarvam-nav-btn:focus-visible {
  outline: 3px solid #6ee7b7;
  outline-offset: 2px;
}

.sarvam-pill {
  background: rgba(255, 255, 255, 0.22);
  padding: 2px 7px;
  border-radius: 10px;
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.3px;
  text-transform: uppercase;
}

.sarvam-sparkle-icon {
  font-size: 0.95rem;
  line-height: 1;
  display: inline-block;
  animation: sarvamSparkle 2.5s infinite ease-in-out;
}

@keyframes sarvamSparkle {
  0%, 100% { transform: scale(1) rotate(0deg); opacity: 1; }
  50% { transform: scale(1.15) rotate(12deg); opacity: 0.85; }
}

/* Screen 2: Quick Sarvam Language Bar */
.sarvam-quick-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  background: linear-gradient(90deg, #eaf6ee 0%, #f4fbf6 100%);
  border: 1px solid #c2e2cc;
  padding: 10px 18px;
  border-radius: var(--radius-sm);
  margin-bottom: 16px;
  font-size: 0.86rem;
}

.sarvam-quick-left {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #176B48;
}

.sarvam-quick-buttons {
  display: flex;
  align-items: center;
  gap: 6px;
}

.sarvam-quick-lang-btn {
  background: #ffffff;
  border: 1px solid #c2e2cc;
  color: var(--color-text);
  padding: 4px 12px;
  border-radius: 16px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all var(--transition);
}

.sarvam-quick-lang-btn:hover {
  border-color: var(--color-primary);
  background: #f0fdf4;
}

.sarvam-quick-lang-btn.active {
  background: var(--color-primary);
  border-color: var(--color-primary);
  color: #ffffff;
}

.sarvam-quick-studio-btn {
  background: transparent;
  border: 1px dashed var(--color-primary);
  color: var(--color-primary);
  padding: 4px 10px;
  border-radius: 16px;
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
  margin-left: 6px;
  transition: all var(--transition);
}

.sarvam-quick-studio-btn:hover {
  background: var(--color-primary);
  color: #ffffff;
}

/* Screen 6: Ticket Actions Sarvam Button */
.btn-sarvam {
  background: linear-gradient(135deg, #176B48 0%, #0c4d32 100%);
  color: #ffffff !important;
  border: none;
  font-weight: 700;
  box-shadow: 0 3px 10px rgba(23, 107, 72, 0.22);
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  border-radius: 8px;
  cursor: pointer;
  transition: all var(--transition);
}

.btn-sarvam:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(23, 107, 72, 0.32);
}

/* Modal Card & Layout */
.sarvam-modal-card {
  max-width: 880px;
  width: 95%;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  border-radius: 18px;
  box-shadow: 0 16px 50px rgba(0, 0, 0, 0.25);
  border: 1px solid var(--color-border);
  overflow: hidden;
}

.sarvam-modal-header {
  background: linear-gradient(135deg, #f3faf5 0%, #e8f4ec 100%);
  border-bottom: 1px solid var(--color-border);
  padding: 20px 24px;
}

.sarvam-title-wrap {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.sarvam-brand-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #176B48;
  color: #ffffff;
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 0.74rem;
  font-weight: 800;
  letter-spacing: 0.5px;
  width: fit-content;
}

.sarvam-model-tag {
  background: rgba(255, 255, 255, 0.25);
  padding: 1px 6px;
  border-radius: 6px;
  font-family: monospace;
  font-size: 0.7rem;
}

.sarvam-modal-header h3 {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--color-text);
  margin-top: 4px;
}

.sarvam-modal-subtitle {
  font-size: 0.84rem;
  color: var(--color-muted);
  line-height: 1.4;
}

.sarvam-modal-body {
  padding: 20px 24px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

/* Language Selection Row */
.sarvam-lang-bar {
  display: flex;
  align-items: flex-end;
  gap: 12px;
  background: var(--color-bg);
  padding: 14px 18px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--color-border);
}

.sarvam-lang-select-group {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sarvam-lang-select-group label {
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--color-muted);
}

.sarvam-select {
  width: 100%;
  padding: 10px 14px;
  border: 1.5px solid var(--color-border);
  border-radius: 8px;
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--color-text);
  background-color: var(--color-white);
  cursor: pointer;
  transition: all var(--transition);
}

.sarvam-select:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(23, 107, 72, 0.15);
}

.sarvam-swap-btn {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--color-white);
  border: 1.5px solid var(--color-border);
  border-radius: 50%;
  font-size: 1.25rem;
  color: var(--color-primary);
  cursor: pointer;
  transition: all var(--transition);
  flex-shrink: 0;
  margin-bottom: 2px;
}

.sarvam-swap-btn:hover {
  background: var(--color-secondary);
  border-color: var(--color-primary);
  transform: rotate(180deg);
}

/* Advanced Controls Row */
.sarvam-controls-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}

.sarvam-control-item {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sarvam-control-item label {
  font-size: 0.76rem;
  font-weight: 700;
  color: var(--color-muted);
}

.sarvam-select-sm {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid var(--color-border);
  border-radius: 6px;
  font-size: 0.84rem;
  font-weight: 500;
  color: var(--color-text);
  background-color: var(--color-white);
}

/* Presets */
.sarvam-presets-section {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.sarvam-presets-title {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--color-muted);
  text-transform: uppercase;
}

.sarvam-preset-chips {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 4px;
}

.sarvam-preset-chip {
  background: var(--color-white);
  border: 1px solid var(--color-border);
  color: var(--color-text);
  padding: 6px 12px;
  border-radius: 14px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all var(--transition);
}

.sarvam-preset-chip:hover {
  background: var(--color-secondary);
  border-color: var(--color-primary);
  color: var(--color-primary);
}

/* Text Panels Grid */
.sarvam-panels-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.sarvam-panel {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: var(--color-white);
  overflow: hidden;
}

.sarvam-panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 14px;
  background: #fbfdfc;
  border-bottom: 1px solid var(--color-border);
}

.sarvam-panel-label {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--color-muted);
}

.sarvam-char-count {
  font-size: 0.72rem;
  color: var(--color-muted);
}

.sarvam-status-indicator {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--color-success);
}

.status-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  display: inline-block;
}

.status-dot.green {
  background-color: var(--color-success);
  box-shadow: 0 0 6px rgba(24, 134, 75, 0.4);
}

.status-dot.orange {
  background-color: var(--color-warning);
  box-shadow: 0 0 6px rgba(217, 154, 37, 0.4);
}

.sarvam-textarea {
  width: 100%;
  height: 170px;
  padding: 12px 14px;
  font-family: inherit;
  font-size: 0.92rem;
  line-height: 1.6;
  border: none;
  resize: none;
  background: transparent;
  color: var(--color-text);
  box-sizing: border-box;
}

.sarvam-textarea:focus {
  outline: none;
}

.sarvam-output-view {
  overflow-y: auto;
  background: #fafcfb;
  white-space: pre-wrap;
  user-select: text;
}

.sarvam-panel-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  background: #fbfdfc;
  border-top: 1px solid var(--color-border);
}

.sarvam-output-actions {
  display: flex;
  gap: 6px;
}

.sarvam-action-btn {
  background: linear-gradient(135deg, #176B48 0%, #0d4a31 100%);
  color: #ffffff;
  font-weight: 700;
}

/* API Config Box */
.sarvam-config-box {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: #f8faf8;
  overflow: hidden;
}

.sarvam-config-summary {
  padding: 10px 14px;
  font-size: 0.84rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: var(--color-text);
}

.sarvam-config-hint {
  font-size: 0.75rem;
  font-weight: 400;
  color: var(--color-muted);
}

.sarvam-config-content {
  padding: 12px 16px;
  border-top: 1px solid var(--color-border);
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: #ffffff;
}

.sarvam-config-row {
  display: flex;
  gap: 12px;
  align-items: center;
}

.sarvam-input-wrap {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sarvam-input-wrap label {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--color-text);
}

.sarvam-config-info {
  font-size: 0.78rem;
  color: var(--color-muted);
  line-height: 1.5;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.sarvam-modal-footer {
  padding: 14px 24px;
  background: var(--color-bg);
  border-top: 1px solid var(--color-border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sarvam-footer-note {
  font-size: 0.8rem;
  color: var(--color-muted);
}

/* Accessibility Mode Adjustments */
body.accessibility-mode .sarvam-nav-btn {
  background: #000000 !important;
  color: #ffff00 !important;
  border: 2px solid #ffff00 !important;
}

body.accessibility-mode .sarvam-quick-bar {
  background: #000000 !important;
  color: #ffffff !important;
  border: 2px solid #ffff00 !important;
}

body.accessibility-mode .sarvam-quick-lang-btn.active {
  background: #ffff00 !important;
  color: #000000 !important;
}

body.accessibility-mode .sarvam-modal-card {
  border: 3px solid #ffffff !important;
}

@media (max-width: 768px) {
  .sarvam-panels-grid {
    grid-template-columns: 1fr;
  }
  .sarvam-controls-row {
    grid-template-columns: 1fr;
  }
  .sarvam-nav-label {
    display: none;
  }
}
}
"""
