def get_html():
    return """
<!-- Accessibility Banner -->
<div id="accessibility-banner" class="accessibility-banner" role="alert">
  <div class="container" style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
    <span>♿ <strong>Accessibility mode is ON</strong> — Larger text, higher contrast, animations reduced.</span>
    <button type="button" id="a11y-banner-close" aria-label="Turn off accessibility mode">Turn Off</button>
  </div>
</div>

<!-- Header -->
<header class="site-header no-print">
  <div class="container header-inner">
    <a href="#" class="brand-logo" id="header-brand-logo" aria-label="EasyRail Home">
      <div class="logo-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="4" y="3" width="16" height="16" rx="2"/>
          <path d="M4 11h16"/>
          <path d="M12 3v8"/>
          <path d="m8 19-2 3"/>
          <path d="m18 22-2-3"/>
          <circle cx="8" cy="15" r="1"/>
          <circle cx="16" cy="15" r="1"/>
        </svg>
      </div>
      <div class="logo-text">
        <h1>EasyRail</h1>
        <span data-i18n="tagline">Your journey, made simple.</span>
      </div>
    </a>

    <nav class="nav-group" aria-label="Main Navigation">
      <ul class="nav-links">
        <li><button type="button" class="nav-link" id="nav-home-btn" data-i18n="navHome">Home</button></li>
        <li>
          <button type="button" class="nav-link" id="nav-bookings-btn">
            <span data-i18n="navBookings">My Bookings</span>
            <span class="badge-count" id="bookings-count-badge">0</span>
          </button>
        </li>
        <li><button type="button" class="nav-link" id="nav-help-btn" data-i18n="navHelp">Help</button></li>
      </ul>

      <div class="header-controls">
        <!-- Language Selector -->
        <div class="lang-dropdown-wrapper">
          <button type="button" class="lang-selector-btn" id="lang-menu-trigger" aria-expanded="false" aria-haspopup="true">
            🌐 <span id="current-lang-label">EN</span> ▾
          </button>
          <div class="lang-menu" id="lang-dropdown-menu" role="menu">
            <div class="lang-menu-heading">App Language</div>
            <button type="button" data-lang="en" class="active">🇬🇧 English (EN)</button>
            <button type="button" data-lang="hi">🇮🇳 हिन्दी (HI)</button>
            <button type="button" data-lang="te">🇮🇳 తెలుగు (TE)</button>
          </div>
        </div>


      </div>
    </nav>
  </div>
</header>

<!-- Progress Stepper (Screens 2 - 6) -->
<section class="stepper-section no-print" id="progress-stepper-section" style="display: none;">
  <div class="container">
    <nav class="stepper-nav" aria-label="Booking Progress">
      <div class="stepper-nav-progress" id="stepper-progress-fill" style="width: 0%;"></div>
      
      <div class="step-item active" data-step="1" id="step-node-1">
        <div class="step-circle">1</div>
        <span class="step-label" data-i18n="stepSearch">Search</span>
      </div>
      <div class="step-item" data-step="2" id="step-node-2">
        <div class="step-circle">2</div>
        <span class="step-label" data-i18n="stepTrain">Select Train</span>
      </div>
      <div class="step-item" data-step="3" id="step-node-3">
        <div class="step-circle">3</div>
        <span class="step-label" data-i18n="stepClass">Choose Class</span>
      </div>
      <div class="step-item" data-step="4" id="step-node-4">
        <div class="step-circle">4</div>
        <span class="step-label" data-i18n="stepPassengers">Passengers</span>
      </div>
      <div class="step-item" data-step="5" id="step-node-5">
        <div class="step-circle">5</div>
        <span class="step-label" data-i18n="stepPayment">Payment</span>
      </div>
      <div class="step-item" data-step="6" id="step-node-6">
        <div class="step-circle">6</div>
        <span class="step-label" data-i18n="stepConfirm">Confirmation</span>
      </div>
    </nav>
  </div>
</section>

<!-- Main App Content -->
<main class="main-content">
  <!-- =====================================================================
       SCREEN 1: Homepage / Search
       ===================================================================== -->
  <section class="screen active" data-screen="1" id="screen-1">
    <div class="hero-section">
      <!-- Decorative Train SVG in Background -->
      <svg class="hero-bg-decoration" viewBox="0 0 400 300" fill="currentColor">
        <path d="M20 180h360v8H20zm0 24h360v4H20zm40-120h280a30 30 0 0 1 30 30v70H30v-70a30 30 0 0 1 30-30zm20 25h50v35H80zm75 0h50v35h-50zm75 0h50v35h-50zm75 0h50v35h-50z"/>
      </svg>
      
      <div class="container">
        <div class="hero-headline">
          <h2 data-i18n="heroTitle">Book your train ticket easily</h2>
          <p data-i18n="heroSubtitle">No confusion. No jargon. Just simple booking.</p>
        </div>

        <div class="search-card-wrapper">
          <div class="search-card">
            <!-- Journey Type Tabs -->
            <div class="journey-tabs" role="tablist">
              <button type="button" class="tab-btn active" id="tab-oneway" role="tab" aria-selected="true" data-i18n="tabOneWay">One Way</button>
            </div>

            <!-- Stations Row -->
            <div class="stations-row">
              <!-- From Station -->
              <div class="station-input-group">
                <label for="from-station-input" class="input-label" data-i18n="labelFrom">From Station</label>
                <div class="input-with-icon">
                  <span class="input-icon">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z"/><circle cx="12" cy="10" r="3"/></svg>
                  </span>
                  <input type="text" id="from-station-input" class="text-input" value="Visakhapatnam (VSKP)" autocomplete="off" placeholder="Enter station name or code" aria-autocomplete="list" aria-expanded="false">
                </div>
                <div class="autocomplete-dropdown" id="from-autocomplete-list"></div>
              </div>

              <!-- Swap Button -->
              <div class="swap-btn-container">
                <button type="button" class="swap-btn" id="swap-stations-btn" title="Swap From and To stations" aria-label="Swap From and To stations">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="m8 3 4 8 5-5 5 15H2L8 3z" style="display:none;"/>
                    <path d="M7 16V4M7 4L3 8M7 4L11 8M17 8V20M17 20L21 16M17 20L13 16"/>
                  </svg>
                </button>
              </div>

              <!-- To Station -->
              <div class="station-input-group">
                <label for="to-station-input" class="input-label" data-i18n="labelTo">To Station</label>
                <div class="input-with-icon">
                  <span class="input-icon">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z"/><circle cx="12" cy="10" r="3"/></svg>
                  </span>
                  <input type="text" id="to-station-input" class="text-input" value="Secunderabad (SC)" autocomplete="off" placeholder="Enter station name or code" aria-autocomplete="list" aria-expanded="false">
                </div>
                <div class="autocomplete-dropdown" id="to-autocomplete-list"></div>
              </div>
            </div>

            <!-- Date & Passengers Row -->
            <div class="details-row">
              <!-- Journey Date -->
              <div>
                <label for="journey-date-input" class="input-label" data-i18n="labelDate">Journey Date</label>
                <div class="input-with-icon">
                  <span class="input-icon">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                  </span>
                  <input type="date" id="journey-date-input" class="text-input" required>
                </div>
              </div>

              <!-- Passengers Stepper -->
              <div>
                <label class="input-label" data-i18n="labelPassengers">Passengers (1-6)</label>
                <div class="stepper-control">
                  <button type="button" class="stepper-btn" id="stepper-minus" aria-label="Decrease passengers">-</button>
                  <div class="stepper-val" id="stepper-count">1</div>
                  <button type="button" class="stepper-btn" id="stepper-plus" aria-label="Increase passengers">+</button>
                </div>
              </div>
            </div>

            <!-- Quota Selection -->
            <div class="quota-row">
              <label class="input-label" data-i18n="labelQuota">Travel Quota</label>
              <div class="quota-grid" role="radiogroup">
                <label class="quota-card active" id="quota-general-card">
                  <input type="radio" name="quota-select" value="General" checked>
                  <span class="quota-icon">👥</span>
                  <span class="quota-title" data-i18n="quotaGeneral">General</span>
                  <span class="quota-desc" data-i18n="quotaGeneralDesc">Standard booking</span>
                </label>

                <label class="quota-card" id="quota-ladies-card">
                  <input type="radio" name="quota-select" value="Ladies">
                  <span class="quota-icon">👩</span>
                  <span class="quota-title" data-i18n="quotaLadies">Ladies</span>
                  <span class="quota-desc" data-i18n="quotaLadiesDesc">Reserved for solo women</span>
                </label>

                <label class="quota-card" id="quota-senior-card">
                  <input type="radio" name="quota-select" value="Senior Citizen">
                  <span class="quota-icon">👴</span>
                  <span class="quota-title" data-i18n="quotaSenior">Senior Citizen</span>
                  <span class="quota-desc" data-i18n="quotaSeniorDesc">Lower berth priority (60+)</span>
                </label>

                <label class="quota-card" id="quota-tatkal-card" title="Tatkal opens at 10 AM for AC, 11 AM for Non-AC">
                  <span class="tatkal-badge">⚡ 10/11 AM</span>
                  <input type="radio" name="quota-select" value="Tatkal">
                  <span class="quota-icon">⚡</span>
                  <span class="quota-title" data-i18n="quotaTatkal">Tatkal</span>
                  <span class="quota-desc" data-i18n="quotaTatkalDesc">Urgent next-day travel</span>
                </label>
              </div>
            </div>

            <!-- Submit Button -->
            <button type="button" class="btn btn-primary btn-lg btn-block" id="search-trains-submit-btn">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
              <span data-i18n="btnSearchTrains">Search Trains</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Help Section (Screen 1) — Inline Accordion -->
    <div class="container help-section">
      <div class="section-header">
        <h3 data-i18n="helpSectionTitle">First time booking? We're here to help.</h3>
        <p data-i18n="helpSectionSubtitle">Tap a question to read the answer.</p>
      </div>

      <div class="faq-accordion" id="faq-accordion">

        <!-- FAQ 1: Coach Classes -->
        <div class="faq-item" id="faq-classes">
          <button type="button" class="faq-trigger" aria-expanded="false" data-faq="classes">
            <div class="faq-trigger-left">
              <span class="faq-icon">🛌</span>
              <span class="faq-question" data-i18n="helpCard1Title">What is SL / 2A / 3A?</span>
            </div>
            <div class="faq-trigger-right">
              <span class="faq-read-more" data-i18n="learnMore">Read more →</span>
              <span class="faq-chevron">▼</span>
            </div>
          </button>
          <div class="faq-body" id="faq-body-classes">
            <div id="faq-content-classes" class="faq-content-inner"></div>
          </div>
        </div>

        <!-- FAQ 2: Availability Codes -->
        <div class="faq-item" id="faq-availability">
          <button type="button" class="faq-trigger" aria-expanded="false" data-faq="availability">
            <div class="faq-trigger-left">
              <span class="faq-icon">🎫</span>
              <span class="faq-question" data-i18n="helpCard2Title">Seat Availability Codes</span>
            </div>
            <div class="faq-trigger-right">
              <span class="faq-read-more" data-i18n="learnMore">Read more →</span>
              <span class="faq-chevron">▼</span>
            </div>
          </button>
          <div class="faq-body" id="faq-body-availability">
            <div id="faq-content-availability" class="faq-content-inner"></div>
          </div>
        </div>

        <!-- FAQ 3: Tatkal -->
        <div class="faq-item" id="faq-tatkal">
          <button type="button" class="faq-trigger" aria-expanded="false" data-faq="tatkal">
            <div class="faq-trigger-left">
              <span class="faq-icon">⚡</span>
              <span class="faq-question" data-i18n="tabTatkalRules">Tatkal Timings &amp; Rules</span>
            </div>
            <div class="faq-trigger-right">
              <span class="faq-read-more" data-i18n="learnMore">Read more →</span>
              <span class="faq-chevron">▼</span>
            </div>
          </button>
          <div class="faq-body" id="faq-body-tatkal">
            <div id="faq-content-tatkal" class="faq-content-inner"></div>
          </div>
        </div>

        <!-- FAQ 4: Payment & Refunds -->
        <div class="faq-item" id="faq-safety">
          <button type="button" class="faq-trigger" aria-expanded="false" data-faq="safety">
            <div class="faq-trigger-left">
              <span class="faq-icon">🛡️</span>
              <span class="faq-question" data-i18n="helpCard3Title">Payment &amp; Refunds</span>
            </div>
            <div class="faq-trigger-right">
              <span class="faq-read-more" data-i18n="learnMore">Read more →</span>
              <span class="faq-chevron">▼</span>
            </div>
          </button>
          <div class="faq-body" id="faq-body-safety">
            <div id="faq-content-safety" class="faq-content-inner"></div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- =====================================================================
       SCREEN 2: Search Results
       ===================================================================== -->
  <section class="screen" data-screen="2" id="screen-2">
    <div class="container" style="padding-top: 24px;">
      <!-- Results Header Bar -->
      <div class="results-header-bar">
        <div class="results-summary-info">
          <button type="button" class="back-btn-circle" id="btn-back-to-search" title="Back to Search" aria-label="Back to Search">
            ←
          </button>
          <div>
            <div class="summary-route" id="results-summary-route">VSKP → SC</div>
            <div class="summary-meta" id="results-summary-meta">22 Nov · 1 Passenger · General Quota</div>
          </div>
        </div>

        <button type="button" class="btn btn-outline" id="btn-modify-search" style="min-height: 40px; padding: 6px 16px;">
          ✏️ <span data-i18n="modifySearch">Modify Search</span>
        </button>
      </div>

      <!-- Filters Row (Optimized for Mobile Phones) -->
      <div class="filter-bar">
        <div class="filter-chips-scroll" role="toolbar" aria-label="Train Filters">
          <button type="button" class="filter-chip active" data-filter="all" data-i18n="filterAll">All Trains</button>
          <button type="button" class="filter-chip" data-filter="morning" data-i18n="filterMorning">Morning (06:00 - 12:00)</button>
          <button type="button" class="filter-chip" data-filter="evening" data-i18n="filterEvening">Evening (18:00 - 24:00)</button>
          <button type="button" class="filter-chip" data-filter="ac" data-i18n="filterAC">AC Only</button>
          <button type="button" class="filter-chip" data-filter="non-ac" data-i18n="filterNonAC">Non-AC</button>
          <button type="button" class="filter-chip" data-filter="available" data-i18n="filterAvailable">Available Only</button>
          <button type="button" class="filter-chip" data-filter="superfast" data-i18n="filterSuperfast">Superfast</button>
        </div>
      </div>

      <!-- Train Cards List -->
      <div class="trains-list" id="trains-list-container">
        <!-- Rendered by JS -->
      </div>

      <!-- No Trains Found State (Hidden by default) -->
      <div class="no-trains-card" id="no-trains-found-card" style="display: none;">
        <div class="no-trains-icon">🚆</div>
        <h3 data-i18n="noTrainsTitle">No trains found for your criteria</h3>
        <p data-i18n="noTrainsDesc">We couldn't find trains matching your filters. Try checking alternative dates or nearby stations below.</p>
        
        <div style="font-weight: 700; margin-bottom: 8px; font-size: 0.9rem;" data-i18n="tryAlternateDates">Try Alternate Dates:</div>
        <div class="alternate-dates-list" id="alternate-dates-chips">
          <!-- Populated by JS -->
        </div>

        <div style="font-weight: 700; margin-bottom: 8px; font-size: 0.9rem;" data-i18n="tryNearbyStations">Or Nearby Stations:</div>
        <div class="popular-chips" style="justify-content: center; margin-bottom: 24px;">
          <button type="button" class="popular-chip" data-nearby="DVD">Duvvada (DVD)</button>
          <button type="button" class="popular-chip" data-nearby="HYB">Hyderabad Deccan (HYB)</button>
          <button type="button" class="popular-chip" data-nearby="BZA">Vijayawada (BZA)</button>
        </div>

        <button type="button" class="btn btn-secondary" id="btn-reset-filters" data-i18n="btnResetFilters">Reset All Filters</button>
      </div>
    </div>
  </section>

  <!-- =====================================================================
       SCREEN 3: Class & Seat Selection
       ===================================================================== -->
  <section class="screen" data-screen="3" id="screen-3">
    <div class="container" style="padding-top: 24px;">
      <!-- Header bar with selected train details -->
      <div class="selection-header-card">
        <div class="results-summary-info">
          <button type="button" class="back-btn-circle" id="btn-back-to-results" title="Back to Results" aria-label="Back to Results">
            ←
          </button>
          <div>
            <div class="summary-route" id="class-screen-train-name">Visakha Express (18645)</div>
            <div class="summary-meta" id="class-screen-train-meta">06:20 VSKP → 14:30 SC (8h 10m) · Daily</div>
          </div>
        </div>

        <div class="status-pill status-available" id="class-screen-quota-badge">
          General Quota
        </div>
      </div>

      <!-- Tatkal Section (Conditional / Interactive) -->
      <div class="tatkal-status-banner" id="tatkal-notice-banner" style="display: none;">
        <div class="tatkal-banner-left">
          <div class="tatkal-clock-icon">⏰</div>
          <div class="tatkal-banner-info">
            <h4 id="tatkal-banner-title">⚡ Tatkal Booking Window</h4>
            <p id="tatkal-banner-desc">AC Tatkal opens at 10:00 AM. Non-AC Tatkal opens at 11:00 AM.</p>
            <div class="tatkal-demo-btns">
              <span style="font-size: 0.72rem; color: #8c5500; font-weight: 700;">Demo Clock:</span>
              <button type="button" class="tatkal-demo-btn" data-time-sim="before10">Before 10 AM</button>
              <button type="button" class="tatkal-demo-btn" data-time-sim="between1011">10:00 - 11:00 AM</button>
              <button type="button" class="tatkal-demo-btn" data-time-sim="after11">After 11 AM</button>
            </div>
          </div>
        </div>
        <div class="tatkal-timer-badge" id="tatkal-countdown-badge">
          Opens in: 02h 15m
        </div>
      </div>

      <div style="margin-bottom: 16px;">
        <h3 style="font-size: 1.35rem; font-weight: 800; color: var(--color-text);" data-i18n="chooseClassTitle">Select Your Travel Class</h3>
        <p style="font-size: 0.9rem; color: var(--color-muted);" data-i18n="chooseClassSubtitle">All available coaches and real-time berth availability for this train.</p>
      </div>

      <!-- Detailed Class Cards Grid -->
      <div class="classes-detail-grid" id="classes-detail-grid">
        <!-- Rendered by JS -->
      </div>
    </div>
  </section>

  <!-- =====================================================================
       SCREEN 4: Passenger Details
       ===================================================================== -->
  <section class="screen" data-screen="4" id="screen-4">
    <div class="container" style="padding-top: 24px;">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
        <div style="display: flex; align-items: center; gap: 12px;">
          <button type="button" class="back-btn-circle" id="btn-back-to-class" title="Back to Class selection">←</button>
          <div>
            <h2 style="font-size: 1.5rem; font-weight: 800; color: var(--color-text);" data-i18n="passengerDetailsTitle">Passenger Details</h2>
            <p style="font-size: 0.85rem; color: var(--color-muted);" data-i18n="passengerDetailsSubtitle">Enter details matching government-issued photo ID cards.</p>
          </div>
        </div>
      </div>

      <!-- Collapsible Journey Summary Card -->
      <div class="booking-summary-accordion">
        <div class="accordion-header" id="journey-summary-accordion-header">
          <div style="display: flex; align-items: center; gap: 10px;">
            <span>📋</span>
            <span id="accordion-title-summary">Journey Summary: Visakha Express (18645) · 3A</span>
          </div>
          <span id="accordion-chevron">▼</span>
        </div>
        <div class="accordion-content" id="journey-summary-accordion-body">
          <div>
            <div class="summary-stat-label" data-i18n="trainName">Train</div>
            <div class="summary-stat-value" id="summary-train-val">18645 Visakha Express</div>
          </div>
          <div>
            <div class="summary-stat-label" data-i18n="route">Route & Date</div>
            <div class="summary-stat-value" id="summary-route-val">VSKP → SC (22 Nov)</div>
          </div>
          <div>
            <div class="summary-stat-label" data-i18n="classQuota">Class & Quota</div>
            <div class="summary-stat-value" id="summary-class-val">AC 3 Tier (3A) · General</div>
          </div>
          <div>
            <div class="summary-stat-label" data-i18n="farePerPerson">Fare Per Person</div>
            <div class="summary-stat-value" id="summary-fare-val">₹1,035</div>
          </div>
        </div>
      </div>

      <!-- Dynamic Passenger Forms -->
      <div class="passenger-forms-container" id="passenger-forms-container">
        <!-- Rendered by JS for 1..N passengers -->
      </div>

      <!-- Contact Details Card -->
      <div class="contact-details-card">
        <h4 style="font-size: 1.15rem; font-weight: 800; margin-bottom: 16px; color: var(--color-text);" data-i18n="contactDetailsTitle">
          Contact Details for E-Ticket & SMS
        </h4>
        <div class="contact-grid">
          <div class="form-group">
            <label for="contact-mobile-input" data-i18n="labelMobile">Mobile Number *</label>
            <div class="mobile-input-wrap">
              <span class="country-code-pill">+91</span>
              <input type="tel" id="contact-mobile-input" class="form-control" placeholder="10-digit mobile number" maxlength="10" value="9876543210" required>
              <span class="input-valid-icon">✓</span>
            </div>
            <div class="error-text" id="mobile-error-msg">Please enter a valid 10-digit Indian mobile number.</div>
          </div>

          <div class="form-group">
            <label for="contact-email-input"><span data-i18n="labelEmail">Email Address</span> <span style="font-weight: 400; color: var(--color-muted);">(Optional)</span></label>
            <div class="form-input-wrap">
              <input type="email" id="contact-email-input" class="form-control" placeholder="For receipt copy (e.g. passenger@gmail.com)" value="passenger@example.com">
              <span class="input-valid-icon">✓</span>
            </div>
          </div>
        </div>

        <div class="contact-notice-box">
          <span>ℹ️</span>
          <span data-i18n="contactNotice">PNR updates, live train running status, and ticket SMS will be delivered to this mobile number.</span>
        </div>
      </div>

      <!-- Submit Action -->
      <div style="display: flex; justify-content: flex-end; margin-bottom: 40px;">
        <button type="button" class="btn btn-primary btn-lg" id="btn-continue-to-payment" style="min-width: 240px;">
          <span data-i18n="continueToPayment">Continue to Payment →</span>
        </button>
      </div>
    </div>
  </section>

  <!-- =====================================================================
       SCREEN 5: Payment
       ===================================================================== -->
  <section class="screen" data-screen="5" id="screen-5">
    <div class="container" style="padding-top: 24px;">
      <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
        <button type="button" class="back-btn-circle" id="btn-back-to-passengers" title="Back to Passenger Details">←</button>
        <div>
          <h2 style="font-size: 1.5rem; font-weight: 800; color: var(--color-text);" data-i18n="paymentTitle">Review & Payment</h2>
          <p style="font-size: 0.85rem; color: var(--color-muted);" data-i18n="paymentSubtitle">100% simulated secure payment for EasyRail Prototype.</p>
        </div>
      </div>

      <!-- Payment Failure State Box (shown when transaction fails) -->
      <div class="payment-failure-box" id="payment-failure-box">
        <div class="failure-header">
          <div class="failure-icon-wrap">✕</div>
          <div>
            <h3 data-i18n="paymentFailed">Payment Failed</h3>
            <p style="font-size: 0.88rem; color: #a12b2b;" data-i18n="bankDeclined">Your bank declined the transaction. (ERR_SIMULATED_DECLINE)</p>
          </div>
        </div>
        <div class="failure-details">
          <div><strong>Transaction ID:</strong> <span id="failed-txn-id">TXN_ERR_78912401</span></div>
          <div style="margin-top: 4px; color: var(--color-success); font-weight: 700;">
            🛡️ <span data-i18n="moneySafe">Your money has NOT been deducted. No reservation was made.</span>
          </div>
        </div>
        <div class="failure-actions">
          <button type="button" class="btn btn-primary" id="btn-try-payment-again" data-i18n="tryAgain">Try Again</button>
          <button type="button" class="btn btn-outline" id="btn-contact-support" data-i18n="contactSupport">Help & FAQs</button>
        </div>
      </div>

      <div class="payment-layout">
        <!-- Payment Methods Card -->
        <div class="payment-methods-card">
          <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 16px; color: var(--color-text);" data-i18n="choosePaymentMethod">
            Select Payment Method
          </h3>

          <div class="payment-tabs-nav" role="tablist">
            <button type="button" class="pay-tab-btn active" data-paytab="upi" data-i18n="tabUPI">UPI / QR</button>
            <button type="button" class="pay-tab-btn" data-paytab="card" data-i18n="tabCard">Debit / Credit Card</button>
            <button type="button" class="pay-tab-btn" data-paytab="netbanking" data-i18n="tabNetBanking">Net Banking</button>
            <button type="button" class="pay-tab-btn" data-paytab="wallets" data-i18n="tabWallets">Wallets</button>
          </div>

          <!-- TAB 1: UPI -->
          <div class="pay-tab-content active" id="paytab-upi">
            <div style="margin-bottom: 16px;">
              <label class="input-label" data-i18n="instantUPI">Instant Pay with Popular UPI Apps</label>
              <div class="upi-apps-grid">
                <button type="button" class="upi-app-btn active" data-upiapp="gpay">
                  <div class="upi-icon-badge" style="background: #e8f0fe; color: #1a73e8;">GPay</div>
                  <span style="font-size: 0.8rem; font-weight: 700;">Google Pay</span>
                </button>
                <button type="button" class="upi-app-btn" data-upiapp="phonepe">
                  <div class="upi-icon-badge" style="background: #efeaf8; color: #5f259f;">PhPe</div>
                  <span style="font-size: 0.8rem; font-weight: 700;">PhonePe</span>
                </button>
                <button type="button" class="upi-app-btn" data-upiapp="paytm">
                  <div class="upi-icon-badge" style="background: #e1f7fc; color: #00b9f5;">Paytm</div>
                  <span style="font-size: 0.8rem; font-weight: 700;">Paytm UPI</span>
                </button>
                <button type="button" class="upi-app-btn" data-upiapp="bhim">
                  <div class="upi-icon-badge" style="background: #fdf3e7; color: #e06d10;">BHIM</div>
                  <span style="font-size: 0.8rem; font-weight: 700;">BHIM UPI</span>
                </button>
              </div>
            </div>

            <div>
              <label for="upi-id-input" class="input-label" data-i18n="orEnterUPI">Or Enter UPI ID / VPA</label>
              <div class="upi-verify-row">
                <input type="text" id="upi-id-input" class="form-control" placeholder="e.g. mobile@upi or username@okaxis" value="passenger@okaxis">
                <button type="button" class="btn btn-outline" id="btn-verify-upi" style="white-space: nowrap;" data-i18n="verify">Verify</button>
              </div>
              <div id="upi-verified-badge" style="font-size: 0.8rem; color: var(--color-success); font-weight: 700; display: none;">
                ✓ Verified: Passenger Name (HDFC Bank)
              </div>
            </div>
          </div>

          <!-- TAB 2: Card -->
          <div class="pay-tab-content" id="paytab-card">
            <div class="card-form-grid">
              <div class="form-group card-number-row">
                <label for="card-number-input" data-i18n="cardNumber">Card Number</label>
                <input type="text" id="card-number-input" class="form-control" placeholder="4532 1234 5678 9012" maxlength="19" value="4532 8901 2345 6789">
              </div>
              <div class="form-group">
                <label for="card-expiry-input" data-i18n="cardExpiry">Valid Thru</label>
                <input type="text" id="card-expiry-input" class="form-control" placeholder="MM/YY" maxlength="5" value="12/28">
              </div>
              <div class="form-group">
                <label for="card-cvv-input" data-i18n="cardCVV">CVV</label>
                <input type="password" id="card-cvv-input" class="form-control" placeholder="123" maxlength="3" value="789">
              </div>
              <div class="form-group card-number-row">
                <label for="card-name-input" data-i18n="cardHolder">Name on Card</label>
                <input type="text" id="card-name-input" class="form-control" placeholder="Full name as printed on card" value="Rahul Sharma">
              </div>
            </div>
            <div class="card-security-note">
              🔒 <span data-i18n="cardSecurity">Your card details are NOT stored. This is a hackathon simulation only.</span>
            </div>
          </div>

          <!-- TAB 3: Net Banking -->
          <div class="pay-tab-content" id="paytab-netbanking">
            <label class="input-label" data-i18n="popularBanks">Popular Banks</label>
            <div class="banks-grid">
              <button type="button" class="bank-item-btn active" data-bank="SBI"><span class="bank-abbr">SBI</span>State Bank</button>
              <button type="button" class="bank-item-btn" data-bank="HDFC"><span class="bank-abbr">HDFC</span>HDFC Bank</button>
              <button type="button" class="bank-item-btn" data-bank="ICICI"><span class="bank-abbr">ICICI</span>ICICI Bank</button>
              <button type="button" class="bank-item-btn" data-bank="AXIS"><span class="bank-abbr">AXIS</span>Axis Bank</button>
              <button type="button" class="bank-item-btn" data-bank="PNB"><span class="bank-abbr">PNB</span>Punjab Natl</button>
              <button type="button" class="bank-item-btn" data-bank="BOB"><span class="bank-abbr">BOB</span>Bank of Baroda</button>
              <button type="button" class="bank-item-btn" data-bank="KOTAK"><span class="bank-abbr">KOTAK</span>Kotak Bank</button>
              <button type="button" class="bank-item-btn" data-bank="CANARA"><span class="bank-abbr">CANARA</span>Canara Bank</button>
            </div>
            <div class="form-group">
              <label for="other-banks-select" data-i18n="allOtherBanks">All Other Banks</label>
              <select id="other-banks-select" class="form-control">
                <option value="">-- Choose from 50+ other Indian banks --</option>
                <option value="Union Bank of India">Union Bank of India</option>
                <option value="Bank of India">Bank of India</option>
                <option value="Indian Bank">Indian Bank</option>
                <option value="IndusInd Bank">IndusInd Bank</option>
                <option value="Federal Bank">Federal Bank</option>
                <option value="IDBI Bank">IDBI Bank</option>
              </select>
            </div>
          </div>

          <!-- TAB 4: Wallets -->
          <div class="pay-tab-content" id="paytab-wallets">
            <div class="wallets-grid">
              <button type="button" class="wallet-btn active" data-wallet="paytm">
                <span style="font-size: 1.4rem;">🔵</span>
                <div>
                  <div style="font-size: 0.95rem;">Paytm Wallet</div>
                  <div style="font-size: 0.75rem; color: var(--color-muted);">Simulated balance: ₹3,500</div>
                </div>
              </button>
              <button type="button" class="wallet-btn" data-wallet="amazon">
                <span style="font-size: 1.4rem;">📦</span>
                <div>
                  <div style="font-size: 0.95rem;">Amazon Pay</div>
                  <div style="font-size: 0.75rem; color: var(--color-muted);">Simulated balance: ₹2,100</div>
                </div>
              </button>
              <button type="button" class="wallet-btn" data-wallet="mobikwik">
                <span style="font-size: 1.4rem;">⚡</span>
                <div>
                  <div style="font-size: 0.95rem;">MobiKwik</div>
                  <div style="font-size: 0.75rem; color: var(--color-muted);">Simulated balance: ₹1,200</div>
                </div>
              </button>
              <button type="button" class="wallet-btn" data-wallet="phonepe">
                <span style="font-size: 1.4rem;">🟣</span>
                <div>
                  <div style="font-size: 0.95rem;">PhonePe Wallet</div>
                  <div style="font-size: 0.75rem; color: var(--color-muted);">Simulated balance: ₹1,800</div>
                </div>
              </button>
            </div>
          </div>
        </div>

        <!-- Fare Breakdown Card (Right) -->
        <div class="fare-breakdown-card">
          <h3 data-i18n="fareBreakdownTitle">Fare Breakdown</h3>
          
          <div class="fare-line-item">
            <span id="fare-base-label">Base Fare (1 Passenger)</span>
            <span id="fare-base-val">₹1,035</span>
          </div>
          <div class="fare-line-item">
            <span data-i18n="resvCharge">Reservation Charge</span>
            <span>₹40</span>
          </div>
          <div class="fare-line-item" id="fare-superfast-row" style="display: none;">
            <span data-i18n="superfastCharge">Superfast Surcharge</span>
            <span>₹45</span>
          </div>
          <div class="fare-line-item" id="fare-tatkal-row" style="display: none;">
            <span data-i18n="tatkalCharge">Tatkal Charge</span>
            <span id="fare-tatkal-val">₹300</span>
          </div>
          <div class="fare-line-item">
            <span data-i18n="gst">GST (5% AC Coaches)</span>
            <span id="fare-gst-val">₹54</span>
          </div>
          <div class="fare-line-item">
            <span data-i18n="convenienceFee">Convenience Fee</span>
            <span>₹15</span>
          </div>

          <div class="fare-line-item total">
            <span data-i18n="totalPayable">Total Amount</span>
            <span id="fare-total-val">₹1,144</span>
          </div>

          <div class="simulated-note-badge" data-i18n="simulatedNote">
            All charges simulated for EasyRail prototype demonstration.
          </div>

          <!-- Hackathon Testing Checkbox -->
          <div class="demo-failure-checkbox-wrap">
            <input type="checkbox" id="check-simulate-failure">
            <label for="check-simulate-failure" data-i18n="demoFailCheck">
              Simulate payment failure (Test decline flow)
            </label>
          </div>

          <button type="button" class="btn btn-primary btn-lg btn-block" id="btn-pay-now">
            🔒 <span id="pay-btn-label">Pay ₹1,144</span>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- =====================================================================
       SCREEN 6: Booking Confirmation & Digital Ticket
       ===================================================================== -->
  <section class="screen" data-screen="6" id="screen-6">
    <div class="container" style="padding-top: 24px;">
      <!-- Celebration Banner -->
      <div class="success-banner no-print">
        <div class="success-animated-icon">✓</div>
        <h2 id="confirmation-banner-title" data-i18n="bookingConfirmedTitle">Booking Confirmed!</h2>
        <p id="confirmation-banner-subtitle" data-i18n="bookingConfirmedSubtitle">Your journey is booked. Have a great and safe trip!</p>
      </div>

      <!-- Digital Ticket Card (Print Ready) -->
      <div class="ticket-wrapper" id="ticket-section">
        <div class="ticket-card" id="digital-ticket-card">
          <!-- Ticket Header -->
          <div class="ticket-header-top">
            <div class="ticket-brand-left">
              <h3>EasyRail Electronic Reservation Slip (ERS)</h3>
            </div>
            <div class="simulated-badge-red">SIMULATED TICKET — NOT FOR ACTUAL TRAVEL</div>
          </div>

          <!-- PNR & Meta Banner -->
          <div class="ticket-pnr-banner">
            <div class="pnr-box-left">
              <span class="pnr-label">Demo PNR:</span>
              <span class="pnr-number" id="ticket-pnr-number">482-9104821</span>
            </div>
            <div class="pnr-meta-right">
              <div class="pnr-meta-date"><strong>Booked On:</strong> <span id="ticket-booking-time">22-Nov-2026 10:15 IST</span></div>
              <div class="pnr-meta-txn">Txn: <span id="ticket-txn-id">TXN_9823102</span></div>
            </div>
          </div>

          <!-- Ticket Body -->
          <div class="ticket-body">
            <!-- Train & Timings Grid -->
            <div class="ticket-journey-grid">
              <div class="journey-node">
                <div class="node-time" id="ticket-dep-time">06:20</div>
                <div class="node-stn-code" id="ticket-dep-code">VSKP</div>
                <div class="node-stn-name" id="ticket-dep-name">Visakhapatnam Jn (PF 1)</div>
                <div style="font-size: 0.8rem; color: var(--color-muted); margin-top: 2px;" id="ticket-journey-date">22 Nov 2026</div>
              </div>

              <div class="journey-mid-train">
                <div class="train-title-big" id="ticket-train-fullname">18645 / Visakha Express</div>
                <div class="train-meta-pill" id="ticket-class-quota-pill">AC 3 Tier (3A) · General Quota</div>
                <div style="font-size: 0.75rem; color: var(--color-muted); margin-top: 4px;" id="ticket-duration-val">8h 10m · 701 km</div>
              </div>

              <div class="journey-node dest">
                <div class="node-time" id="ticket-arr-time">14:30</div>
                <div class="node-stn-code" id="ticket-arr-code">SC</div>
                <div class="node-stn-name" id="ticket-arr-name">Secunderabad Jn (PF 3)</div>
                <div style="font-size: 0.8rem; color: var(--color-muted); margin-top: 2px;" id="ticket-arrival-date">22 Nov 2026</div>
              </div>
            </div>

            <!-- Passengers Table -->
            <div class="ticket-passengers-table-wrap">
              <table class="ticket-table" aria-label="Booked Passengers List">
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Passenger Name</th>
                    <th>Age / Gender</th>
                    <th>Coach</th>
                    <th>Berth / Seat</th>
                    <th>Berth Type</th>
                    <th>Current Status</th>
                  </tr>
                </thead>
                <tbody id="ticket-passengers-tbody">
                  <!-- Rendered by JS -->
                </tbody>
              </table>
            </div>

            <!-- Security, QR & Fare Footer -->
            <div class="ticket-security-footer">
              <div class="qr-code-placeholder">
                <!-- Decorative SVG QR Code -->
                <svg class="qr-svg" viewBox="0 0 100 100" fill="currentColor">
                  <path d="M0 0h30v30H0zm6 6h18v18H6zm34-6h20v20H40zm30 0h30v30H70zm6 6h18v18H76zm-76 70h30v30H0zm6 6h18v18H6zm44-6h10v10H50zm20 0h10v10H70zm20 0h10v10H90zm-40 20h20v10H50zm30 0h20v10H80zm-40-50h10v10H40zm20 0h10v10H60zm-10 10h10v10H50zm20 0h10v10H70zm-30 10h10v10H40zm30 0h10v10H70z"/>
                </svg>
                <div class="qr-caption">
                  <div><strong>Verify Ticket</strong></div>
                  <span style="font-size: 0.72rem;">Scan with EasyRail inspector app to verify digital signature and ID verification status.</span>
                </div>
              </div>

              <div class="ticket-total-fare">
                <div class="ticket-fare-label" data-i18n="totalFarePaid">Total Fare Paid</div>
                <div class="ticket-fare-val" id="ticket-fare-paid-val">₹1,144</div>
                <div style="font-size: 0.75rem; color: var(--color-success); font-weight: 700;">✓ Payment Confirmed</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="ticket-actions-bar no-print">
        <button type="button" class="btn btn-primary" id="btn-print-ticket">
          🖨️ <span data-i18n="printTicket">Print Ticket</span>
        </button>
        <button type="button" class="btn btn-secondary" id="btn-download-ticket">
          📥 <span data-i18n="downloadTicket">Download Ticket</span>
        </button>
        <button type="button" class="btn btn-outline" id="btn-share-ticket">
          📤 <span data-i18n="shareTicket">Share Ticket</span>
        </button>
        <button type="button" class="btn btn-outline" id="btn-book-another">
          🏠 <span data-i18n="bookAnother">Book Another Journey</span>
        </button>
      </div>

      <!-- Hackathon Disclaimer -->
      <div class="hackathon-disclaimer no-print">
        <strong>Important Notice:</strong> This is a demo booking made on the <strong>EasyRail</strong> hackathon prototype. No real money has been transferred and no actual reservation has been made in Indian Railways IRCTC systems.
      </div>
    </div>
  </section>
</main>

<!-- =====================================================================
     MODALS & DRAWERS
     ===================================================================== -->

<!-- 1. Waitlist (WL) Advisory Modal -->
<div class="modal-overlay" id="modal-wl-advisory" role="dialog" aria-modal="true" aria-labelledby="wl-modal-title">
  <div class="modal-card">
    <div class="modal-header">
      <h3 id="wl-modal-title" style="display: flex; align-items: center; gap: 8px; color: var(--color-warning);">
        <span>⚠️</span> Waitlist Ticket Advisory
      </h3>
      <button type="button" class="modal-close-btn" data-close-modal="modal-wl-advisory" aria-label="Close">✕</button>
    </div>
    <div class="modal-body">
      <div style="background: #fff8eb; border: 1.5px solid #f3d18c; border-radius: 8px; padding: 14px; margin-bottom: 16px;">
        <h4 style="color: #925c04; margin-bottom: 6px; font-size: 1.05rem;" id="wl-modal-status-heading">This train is on Waitlist (WL-34)</h4>
        <p style="font-size: 0.9rem; color: #6e4808; line-height: 1.5;">
          Your berth is <strong>NOT confirmed</strong>. You will be able to board only if other confirmed passengers cancel their tickets prior to chart preparation.
        </p>
      </div>

      <div style="font-size: 0.9rem; color: var(--color-text); line-height: 1.6; display: flex; flex-direction: column; gap: 10px;">
        <div>✅ <strong>100% Refund Guarantee:</strong> If your ticket fails to confirm when charts are prepared (4 hours before departure), your entire fare will be refunded automatically to your bank account.</div>
        <div>ℹ️ <strong>Alternate Recommendation:</strong> You can choose another train with guaranteed seats or continue booking this waitlisted ticket.</div>
      </div>
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-outline" id="btn-wl-choose-another">Choose Another Train</button>
      <button type="button" class="btn btn-primary" id="btn-wl-continue">Continue with Waitlist</button>
    </div>
  </div>
</div>

<!-- 2. Passenger Confirmation Dialog Modal -->
<div class="modal-overlay" id="modal-passenger-confirm" role="dialog" aria-modal="true" aria-labelledby="confirm-modal-title">
  <div class="modal-card">
    <div class="modal-header">
      <h3 id="confirm-modal-title" data-i18n="confirmPassengerTitle">Confirm Passenger Information</h3>
      <button type="button" class="modal-close-btn" data-close-modal="modal-passenger-confirm" aria-label="Close">✕</button>
    </div>
    <div class="modal-body">
      <div style="background: #fdf5e7; border-left: 4px solid var(--color-warning); padding: 12px 16px; margin-bottom: 16px; font-size: 0.88rem; color: #7e4b02;">
        ⚠️ <strong data-i18n="irctcPolicyNote">Important IRCTC Policy:</strong> <span data-i18n="irctcPolicyText">Passenger name, age, and gender corrections are strictly not permitted after ticket confirmation. Please double check accuracy against government ID proof.</span>
      </div>

      <div id="confirm-passengers-preview-list" style="margin-bottom: 16px; border: 1px solid var(--color-border); border-radius: 8px; overflow: hidden;">
        <!-- Filled by JS -->
      </div>

      <p style="font-size: 0.85rem; color: var(--color-muted);" data-i18n="aadhaarVerifyNote">
        By proceeding, you verify that all passenger details match their respective Aadhaar or official photo identity cards.
      </p>
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-outline" data-close-modal="modal-passenger-confirm" data-i18n="btnEditDetails">Edit Details</button>
      <button type="button" class="btn btn-primary" id="btn-confirm-proceed-pay" data-i18n="btnProceedPay">Proceed to Payment →</button>
    </div>
  </div>
</div>

<!-- 3. Comprehensive Help Modal -->
<div class="modal-overlay" id="modal-help-guide" role="dialog" aria-modal="true" aria-labelledby="help-modal-title">
  <div class="modal-card" style="max-width: 720px;">
    <div class="modal-header">
      <h3 id="help-modal-title" data-i18n="helpModalTitle">EasyRail Railway Guide & FAQ</h3>
      <button type="button" class="modal-close-btn" data-close-modal="modal-help-guide" aria-label="Close">✕</button>
    </div>
    <div class="modal-body">
      <div class="help-modal-tabs">
        <button type="button" class="help-modal-tab-btn active" data-helptab="classes" data-i18n="tabCoachClasses">Coach Classes (SL, 3A, 2A...)</button>
        <button type="button" class="help-modal-tab-btn" data-helptab="availability" data-i18n="tabSeatAvailability">Seat Availability Codes</button>
        <button type="button" class="help-modal-tab-btn" data-helptab="tatkal" data-i18n="tabTatkalRules">Tatkal Timings & Rules</button>
        <button type="button" class="help-modal-tab-btn" data-helptab="safety" data-i18n="tabPaymentRefunds">Payment & Refunds</button>
      </div>

      <!-- Tab Content: dynamically rendered by openHelpModal() based on language -->
      <div id="help-tab-content-container"></div>
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-primary" data-close-modal="modal-help-guide">Got It</button>
    </div>
  </div>
</div>

<!-- 4. My Bookings Drawer -->
<div class="bookings-drawer" id="bookings-drawer" role="dialog" aria-modal="true" aria-labelledby="drawer-title">
  <div class="drawer-header">
    <h3 id="drawer-title" style="display: flex; align-items: center; gap: 8px;">
      <span>🎟️</span> <span data-i18n="myBookingsTitle">My Bookings</span>
    </h3>
    <button type="button" class="modal-close-btn" id="btn-close-bookings-drawer" aria-label="Close My Bookings">✕</button>
  </div>
  <div class="drawer-content" id="drawer-bookings-list">
    <!-- Populated by JS -->
  </div>
</div>

<!-- Refund Status Tracker Modal -->
<div class="modal-overlay" id="modal-refund-status" role="dialog" aria-modal="true" aria-labelledby="refund-modal-title" style="display: none;">
  <div class="modal-card" style="max-width: 520px;">
    <div class="modal-header">
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 1.3rem;">💳</span>
        <h3 id="refund-modal-title" style="margin: 0; font-size: 1.15rem;">Cancellation &amp; Refund Tracker</h3>
      </div>
      <button type="button" class="modal-close-btn" data-close-modal="modal-refund-status" aria-label="Close">✕</button>
    </div>
    <div class="modal-body" id="refund-modal-body" style="padding: 16px 20px;">
      <!-- Populated dynamically by JS -->
    </div>
    <div class="modal-footer" style="padding: 12px 20px;">
      <button type="button" class="btn btn-primary btn-block" data-close-modal="modal-refund-status">Close Tracker</button>
    </div>
  </div>
</div>

<!-- Payment Processing Overlay -->
<div class="processing-overlay" id="payment-processing-overlay" role="alert" aria-busy="true">
  <div class="processing-card">
    <div class="processing-spinner"></div>
    <h3 id="processing-title" data-i18n="procTitle">Processing Your Payment...</h3>
    <p id="processing-status-text" data-i18n="procStatus">Connecting with secure payment gateway...</p>
    <div style="margin-top: 16px; font-size: 0.78rem; color: var(--color-muted);">
      Please do not refresh the page or press the back button.
    </div>
  </div>
</div>

<!-- Toast Container -->
<div class="toast-container" id="toast-container" role="status" aria-live="polite"></div>
"""
