def get_js():
    return r"""
/* ==========================================================================
   EasyRail Application Logic & State Architecture
   ========================================================================== */

// --- 1. Realistic Train Dataset (Exactly matching Hackathon prompt) ---
const trains = [
  { 
    id: 1, 
    name: "Visakha Express", 
    number: "18645", 
    dep: "06:20", 
    arr: "14:30", 
    duration: "8h 10m", 
    days: "Daily", 
    runningDaysArray: ["M", "T", "W", "T", "F", "S", "S"],
    classes: [
      { code: "SL", name: "Sleeper", fare: 395, avail: 48, status: "AVAILABLE" },
      { code: "3A", name: "AC 3 Tier", fare: 1035, avail: 12, status: "AVAILABLE" },
      { code: "2A", name: "AC 2 Tier", fare: 1480, avail: 4, status: "AVAILABLE" },
      { code: "1A", name: "AC First", fare: 2495, avail: 2, status: "AVAILABLE" }
    ], 
    type: "Express",
    originCode: "VSKP",
    originName: "Visakhapatnam Jn (Platform 1)",
    destCode: "SC",
    destName: "Secunderabad Jn (Platform 3)",
    distance: "701 km"
  },
  { 
    id: 2, 
    name: "East Coast Express", 
    number: "18645", 
    dep: "10:45", 
    arr: "19:50", 
    duration: "9h 05m", 
    days: "Daily", 
    runningDaysArray: ["M", "T", "W", "T", "F", "S", "S"],
    classes: [
      { code: "SL", name: "Sleeper", fare: 365, avail: 0, wl: 34, status: "WL" },
      { code: "3A", name: "AC 3 Tier", fare: 995, avail: 2, status: "RAC" },
      { code: "2A", name: "AC 2 Tier", fare: 1420, avail: 0, wl: 12, status: "WL" }
    ], 
    type: "Express",
    originCode: "VSKP",
    originName: "Visakhapatnam Jn (Platform 4)",
    destCode: "SC",
    destName: "Secunderabad Jn (Platform 1)",
    distance: "701 km"
  },
  { 
    id: 3, 
    name: "Godavari SF Express", 
    number: "12727", 
    dep: "15:30", 
    arr: "22:15", 
    duration: "6h 45m", 
    days: "Mon Wed Fri Sat", 
    runningDaysArray: ["M", "W", "F", "S"],
    classes: [
      { code: "CC", name: "Chair Car", fare: 285, avail: 62, status: "AVAILABLE" },
      { code: "SL", name: "Sleeper", fare: 375, avail: 28, status: "AVAILABLE" },
      { code: "3A", name: "AC 3 Tier", fare: 1010, avail: 0, wl: 8, status: "WL" }
    ], 
    type: "Superfast",
    originCode: "VSKP",
    originName: "Visakhapatnam Jn (Platform 1)",
    destCode: "SC",
    destName: "Secunderabad Jn (Platform 2)",
    distance: "701 km"
  },
  { 
    id: 4, 
    name: "Konark Express", 
    number: "11019", 
    dep: "20:15", 
    arr: "06:40+1", 
    duration: "10h 25m", 
    days: "Daily", 
    runningDaysArray: ["M", "T", "W", "T", "F", "S", "S"],
    classes: [
      { code: "SL", name: "Sleeper", fare: 380, avail: 92, status: "AVAILABLE" },
      { code: "3A", name: "AC 3 Tier", fare: 1020, avail: 31, status: "AVAILABLE" },
      { code: "2A", name: "AC 2 Tier", fare: 1460, avail: 8, status: "AVAILABLE" }
    ], 
    type: "Express",
    originCode: "VSKP",
    originName: "Visakhapatnam Jn (Platform 2)",
    destCode: "SC",
    destName: "Secunderabad Jn (Platform 5)",
    distance: "701 km"
  },
  { 
    id: 5, 
    name: "Tatkal Special", 
    number: "02727", 
    dep: "06:00", 
    arr: "13:30", 
    duration: "7h 30m", 
    days: "Daily", 
    runningDaysArray: ["M", "T", "W", "T", "F", "S", "S"],
    classes: [
      { code: "SL", name: "Sleeper", fare: 620, avail: 15, status: "AVAILABLE" },
      { code: "3A", name: "AC 3 Tier", fare: 1480, avail: 5, status: "AVAILABLE" }
    ], 
    type: "Tatkal",
    originCode: "VSKP",
    originName: "Visakhapatnam Jn (Platform 3)",
    destCode: "SC",
    destName: "Secunderabad Jn (Platform 4)",
    distance: "701 km"
  }
];

const trainsDB = trains;

// --- 2. Station Database (16 major Indian railway hubs) ---
const stationsDB = [
  { code: "VSKP", name: "Visakhapatnam Junction", city: "Visakhapatnam", state: "Andhra Pradesh" },
  { code: "SC", name: "Secunderabad Junction", city: "Secunderabad", state: "Telangana" },
  { code: "NDLS", name: "New Delhi Railway Station", city: "New Delhi", state: "Delhi" },
  { code: "HWH", name: "Howrah Junction", city: "Kolkata", state: "West Bengal" },
  { code: "MAS", name: "MGR Chennai Central", city: "Chennai", state: "Tamil Nadu" },
  { code: "CSMT", name: "Chhatrapati Shivaji Maharaj Terminus", city: "Mumbai", state: "Maharashtra" },
  { code: "BZA", name: "Vijayawada Junction", city: "Vijayawada", state: "Andhra Pradesh" },
  { code: "SBC", name: "KSR Bengaluru City", city: "Bengaluru", state: "Karnataka" },
  { code: "PUNE", name: "Pune Junction", city: "Pune", state: "Maharashtra" },
  { code: "ADI", name: "Ahmedabad Junction", city: "Ahmedabad", state: "Gujarat" },
  { code: "PNBE", name: "Patna Junction", city: "Patna", state: "Bihar" },
  { code: "JP", name: "Jaipur Junction", city: "Jaipur", state: "Rajasthan" },
  { code: "HYB", name: "Hyderabad Deccan (Nampally)", city: "Hyderabad", state: "Telangana" },
  { code: "GHY", name: "Guwahati Railway Station", city: "Guwahati", state: "Assam" },
  { code: "TVC", name: "Thiruvananthapuram Central", city: "Trivandrum", state: "Kerala" },
  { code: "DVD", name: "Duvvada Station", city: "Visakhapatnam", state: "Andhra Pradesh" }
];

// --- 3. Global Application State ---
const appState = {
  // Navigation
  currentScreen: 1,
  
  // Search state
  from: 'VSKP',
  to: 'SC',
  fromStation: { code: 'VSKP', name: 'Visakhapatnam Junction', city: 'Visakhapatnam' },
  toStation: { code: 'SC', name: 'Secunderabad Junction', city: 'Secunderabad' },
  date: '',
  journeyDate: '',
  passengers: 1,
  passengerCount: 1,
  passengersCount: 1,
  quota: 'General',
  tatkalMode: false,
  
  // Selection
  selectedTrain: null,
  selectedClass: null,
  pendingWLClass: null,
  
  // Passenger Details
  passengersList: [],
  contact: {
    mobile: '9876543210',
    email: 'passenger@example.com'
  },
  
  // Payment
  paymentMethod: 'upi',
  upiApp: 'gpay',
  selectedBank: 'SBI',
  selectedWallet: 'paytm',
  fareBreakdown: {
    baseFare: 0,
    reservationFee: 40,
    superfastFee: 0,
    tatkalFee: 0,
    gst: 0,
    convenienceFee: 15,
    total: 0
  },
  
  // Booking confirmation
  pnr: '',
  bookingStatus: 'CONFIRMED',
  bookingTime: '',
  transactionId: '',
  bookingsHistory: [],
  
  // Modes & Settings
  language: 'en',
  accessibilityMode: false,
  simulateTatkalClock: 'before10', // 'before10', 'between1011', 'after11'
  currentFilter: 'all',
  noResultsDemo: false,
  isProcessingPayment: false
};

// --- 4. Class Descriptions and Berth Layouts ---
const classDescriptions = {
  SL: {
    fullName: "Sleeper Class",
    badge: "Non-AC Berths",
    desc: "Sleeper Class — Non-AC berths. Upper, middle and lower berths. Best value for longer journeys.",
    icon: "🛌"
  },
  "3A": {
    fullName: "AC 3 Tier",
    badge: "Air-Conditioned",
    desc: "AC 3 Tier — Air-conditioned coach with 3 berths per bay. Comfortable for overnight travel.",
    icon: "❄️"
  },
  "2A": {
    fullName: "AC 2 Tier",
    badge: "Air-Conditioned",
    desc: "AC 2 Tier — Air-conditioned coach with 2 berths per bay. More privacy, wider berths.",
    icon: "✨"
  },
  "1A": {
    fullName: "AC First Class",
    badge: "Luxury Cabin",
    desc: "AC First Class — Private cabin with 2 or 4 berths. Premium comfort.",
    icon: "👑"
  },
  CC: {
    fullName: "AC Chair Car",
    badge: "Reclining Seats",
    desc: "Chair Car — Comfortable reclining seats. Ideal for daytime journeys under 5 hours.",
    icon: "💺"
  }
};

// --- 5. Internationalization Dictionary (i18n) ---
const i18n = {
  en: {
    searchBtn: "Search Trains",
    from: "From Station",
    to: "To Station",
    tagline: "Your journey, made simple.",
    navHome: "Home",
    navBookings: "My Bookings",
    navHelp: "Help",
    stepSearch: "Search",
    stepTrain: "Select Train",
    stepClass: "Choose Class",
    stepPassengers: "Passengers",
    stepPayment: "Payment",
    stepConfirm: "Confirmation",
    heroTitle: "Book your train ticket easily",
    heroSubtitle: "No confusion. No jargon. Just simple booking.",
    tabOneWay: "One Way",
    tabRoundTrip: "Round Trip",
    roundTripNotice: "(Coming Soon)",
    labelFrom: "From Station",
    labelTo: "To Station",
    popular: "Popular:",
    labelDate: "Journey Date",
    today: "Today",
    tomorrow: "Tomorrow",
    dayAfter: "Day After",
    labelPassengers: "Passengers (1-6)",
    labelQuota: "Travel Quota",
    quotaGeneral: "General",
    quotaGeneralDesc: "Standard booking",
    quotaLadies: "Ladies",
    quotaLadiesDesc: "Reserved for solo women",
    quotaSenior: "Senior Citizen",
    quotaSeniorDesc: "Lower berth priority (60+)",
    quotaTatkal: "Tatkal",
    quotaTatkalDesc: "Urgent next-day travel",
    btnSearchTrains: "Search Trains",
    helpSectionTitle: "First time booking? We're here to help.",
    helpSectionSubtitle: "Clear answers to common questions about Indian Railways tickets.",
    helpCard1Title: "What is SL / 2A / 3A?",
    helpCard1Desc: "Demystify train coach categories: Sleeper vs 3-Tier AC vs 2-Tier AC, berth arrangements, and what suits your trip best.",
    helpCard2Title: "Understanding Seat Availability",
    helpCard2Desc: "Confused between Available, RAC (Reservation Against Cancellation), and Waitlist (WL)? See how ticket confirmation works.",
    helpCard3Title: "Payment Safety & Refunds",
    helpCard3Desc: "Learn about instant refund processing for unconfirmed waitlisted tickets, secure UPI authentication, and bank safety.",
    learnMore: "Learn more →",
    modifySearch: "Modify Search",
    filterAll: "All Trains",
    filterMorning: "Morning (06:00 - 12:00)",
    filterEvening: "Evening (18:00 - 24:00)",
    filterAC: "AC Only",
    filterNonAC: "Non-AC",
    filterAvailable: "Available Only",
    filterSuperfast: "Superfast",
    toggleNoTrainsDemo: "Demo: Toggle 'No Trains' State",
    noTrainsTitle: "No trains found for your criteria",
    noTrainsDesc: "We couldn't find trains matching your filters. Try checking alternative dates or nearby stations below.",
    tryAlternateDates: "Try Alternate Dates:",
    tryNearbyStations: "Or Nearby Stations:",
    btnResetFilters: "Reset All Filters",
    chooseClassTitle: "Select Your Travel Class",
    chooseClassSubtitle: "All available coaches and real-time berth availability for this train.",
    passengerDetailsTitle: "Passenger Details",
    passengerDetailsSubtitle: "Enter details matching government-issued photo ID cards.",
    trainName: "Train",
    route: "Route & Date",
    classQuota: "Class & Quota",
    farePerPerson: "Fare Per Person",
    contactDetailsTitle: "Contact Details for E-Ticket & SMS",
    labelMobile: "Mobile Number *",
    labelEmail: "Email Address",
    contactNotice: "PNR updates, live train running status, and ticket SMS will be delivered to this mobile number.",
    continueToPayment: "Continue to Payment →",
    paymentTitle: "Review & Payment",
    paymentSubtitle: "100% simulated secure payment for EasyRail Prototype.",
    paymentFailed: "Payment Failed",
    bankDeclined: "Your bank declined the transaction. (ERR_SIMULATED_DECLINE)",
    moneySafe: "Your money has NOT been deducted. No reservation was made.",
    tryAgain: "Try Again",
    contactSupport: "Help & FAQs",
    choosePaymentMethod: "Select Payment Method",
    instantUPI: "Instant Pay with Popular UPI Apps",
    orEnterUPI: "Or Enter UPI ID / VPA",
    verify: "Verify",
    cardNumber: "Card Number",
    cardExpiry: "Valid Thru",
    cardCVV: "CVV",
    cardHolder: "Name on Card",
    cardSecurity: "Your card details are NOT stored. This is a hackathon simulation only.",
    popularBanks: "Popular Banks",
    allOtherBanks: "All Other Banks",
    fareBreakdownTitle: "Fare Breakdown",
    resvCharge: "Reservation Charge",
    superfastCharge: "Superfast Surcharge",
    tatkalCharge: "Tatkal Charge",
    gst: "GST (5% AC Coaches)",
    convenienceFee: "Convenience Fee",
    totalPayable: "Total Amount",
    simulatedNote: "All charges simulated for EasyRail prototype demonstration.",
    demoFailCheck: "Simulate payment failure (Test decline flow)",
    bookingConfirmedTitle: "Booking Confirmed!",
    bookingConfirmedSubtitle: "Your journey is booked. Have a great and safe trip!",
    totalFarePaid: "Total Fare Paid",
    printTicket: "Print Ticket",
    downloadTicket: "Download Ticket",
    shareTicket: "Share Ticket",
    bookAnother: "Book Another Journey",
    myBookingsTitle: "My Bookings",
    translateTicket: "Translate Ticket (Sarvam AI)",
    bookNow: "Book Now →",
    runsDaily: "Runs Daily",
    runsOnDays: "Runs on selected days",
    overnightTag: "+1 Day",
    catering: "⚡ E-Catering",
    charging: "🔌 Mobile Charging",
    security: "🛡️ On-Board Security",
    statusAvailable: "AVL",
    statusRAC: "RAC",
    statusWL: "WL",
    immediateConfirm: "Immediate Confirmation: Berths are available for immediate confirmation upon payment.",
    racNote: "RAC: You'll get a seat on the train. Berth upgrade possible if cancellations happen.",
    wlNote: "Waitlisted: Your berth is not guaranteed. We'll notify you if confirmed. 100% refund if unconfirmed.",
    selectThisClass: "Select this class →",
    passenger: "Passenger",
    adultNotice: "Adult (Above 5 yrs)",
    fullNameLabel: "Full Name *",
    fullNamePlaceholder: "As per ID proof",
    ageLabel: "Age *",
    genderLabel: "Gender *",
    genderMale: "Male",
    genderFemale: "Female",
    genderOther: "Other",
    berthPrefLabel: "Berth Preference",
    berthSubject: "(Subject to availability)",
    noPref: "No Preference",
    lowerBerth: "Lower",
    middleBerth: "Middle",
    upperBerth: "Upper",
    sideLowerBerth: "Side Lower",
    sideUpperBerth: "Side Upper",
    valNameError: "Please enter a valid full name.",
    valAgeError: "Enter age 1-99.",
    valMobileError: "Please enter a valid 10-digit mobile number.",
    ticketConfirmedBanner: "Booking Confirmed!",
    ticketConfirmedSub: "Your journey is booked. Have a great trip!",
    waitlistBanner: "Waitlist Ticket Issued",
    waitlistSub: "Your waitlisted ticket has been generated. Seat confirmation updates will be sent via SMS.",
    verifyTicket: "Verify Ticket",
    verifyTicketDesc: "Scan with EasyRail inspector app to verify digital signature and ID verification status.",
    pnrLabel: "PNR Number",
    bookingTimeLabel: "Booked On",
    txnIdLabel: "Transaction ID",
    paymentSuccessLabel: "✓ Payment Confirmed",
    coachBerthLabel: "Coach & Berth",
    baseFare: "Base Fare",
    quickLangNotice: "Language changed to",
    tatkalBadgeTime: "⚡ 10/11 AM",
    tabUPI: "UPI / QR",
    tabCard: "Debit / Credit Card",
    tabNetBanking: "Net Banking",
    tabWallets: "Wallets",
    confirmPassengerTitle: "Confirm Passenger Information",
    irctcPolicyNote: "Important IRCTC Policy:",
    irctcPolicyText: "Passenger name, age, and gender corrections are strictly not permitted after ticket confirmation. Please double check accuracy against government ID proof.",
    aadhaarVerifyNote: "By proceeding, you verify that all passenger details match their respective Aadhaar or official photo identity cards.",
    btnEditDetails: "Edit Details",
    btnProceedPay: "Proceed to Payment →",
    helpModalTitle: "EasyRail Railway Guide & FAQ",
    tabCoachClasses: "Coach Classes (SL, 3A, 2A...)",
    tabSeatAvailability: "Seat Availability Codes",
    tabTatkalRules: "Tatkal Timings & Rules",
    tabPaymentRefunds: "Payment & Refunds",
    btnGotIt: "Got It",
    journeySummary: "Journey Summary",
    noBookingsYet: "No Bookings Yet",
    noBookingsDesc: "Your booked journey tickets will appear here for easy access and re-printing.",
    stationWord: "Station",
    platformWord: "Platform",
    hoursWord: "hours",
    minsWord: "mins",
    dailyWord: "Daily"
  },
  hi: {
    searchBtn: "ट्रेन खोजें",
    from: "प्रस्थान स्टेशन",
    to: "गंतव्य स्टेशन",
    tagline: "आपकी यात्रा, अब बिल्कुल आसान।",
    navHome: "होम",
    navBookings: "मेरी बुकिंग",
    navHelp: "सहायता",
    stepSearch: "खोजें",
    stepTrain: "ट्रेन चुनें",
    stepClass: "श्रेणी चुनें",
    stepPassengers: "यात्री",
    stepPayment: "भुगतान",
    stepConfirm: "पुष्टि",
    heroTitle: "अपनी ट्रेन टिकट आसानी से बुक करें",
    heroSubtitle: "कोई भ्रम नहीं। कोई जटिलता नहीं। बस सरल बुकिंग।",
    tabOneWay: "एक तरफ",
    tabRoundTrip: "राउंड ट्रिप",
    roundTripNotice: "(जल्द आ रहा है)",
    labelFrom: "प्रस्थान स्टेशन",
    labelTo: "गंतव्य स्टेशन",
    popular: "लोकप्रिय:",
    labelDate: "यात्रा तिथि",
    today: "आज",
    tomorrow: "कल",
    dayAfter: "परसों",
    labelPassengers: "यात्री (1-6)",
    labelQuota: "यात्रा कोटा",
    quotaGeneral: "सामान्य",
    quotaGeneralDesc: "मानक बुकिंग",
    quotaLadies: "महिला",
    quotaLadiesDesc: "महिला यात्रियों के लिए",
    quotaSenior: "वरिष्ठ नागरिक",
    quotaSeniorDesc: "निचली बर्थ प्राथमिकता (60+)",
    quotaTatkal: "तत्काल",
    quotaTatkalDesc: "आपातकालीन यात्रा",
    btnSearchTrains: "ट्रेन खोजें",
    helpSectionTitle: "पहली बार टिकट बुक कर रहे हैं? हम आपकी मदद के लिए हैं।",
    helpSectionSubtitle: "भारतीय रेलवे टिकटों के बारे में सरल और स्पष्ट जानकारी।",
    helpCard1Title: "SL / 2A / 3A क्या है?",
    helpCard1Desc: "स्लीपर, 3-टियर एसी और 2-टियर एसी डिब्बों के बीच का अंतर आसानी से समझें।",
    helpCard2Title: "सीट उपलब्धता को समझें",
    helpCard2Desc: "कन्फर्म, आरएसी (RAC) और वेटलिस्ट (WL) के बीच अंतर जानें।",
    helpCard3Title: "सुरक्षित भुगतान और रिफंड",
    helpCard3Desc: "अपुष्ट वेटलिस्ट टिकटों पर तुरंत रिफंड और सुरक्षित भुगतान प्रणाली की जानकारी।",
    learnMore: "और जानें →",
    modifySearch: "खोज बदलें",
    filterAll: "सभी ट्रेनें",
    filterMorning: "सुबह (06:00 - 12:00)",
    filterEvening: "शाम (18:00 - 24:00)",
    filterAC: "केवल एसी",
    filterNonAC: "नॉन-एसी",
    filterAvailable: "केवल उपलब्ध",
    filterSuperfast: "सुपरफास्ट",
    toggleNoTrainsDemo: "डेमो: 'कोई ट्रेन नहीं' स्थिति देखें",
    noTrainsTitle: "कोई ट्रेन नहीं मिली",
    noTrainsDesc: "आपके फ़िल्टर के अनुसार कोई ट्रेन उपलब्ध नहीं है। कृपया अन्य तारीखें या नजदीकी स्टेशन देखें।",
    tryAlternateDates: "अन्य तारीखें देखें:",
    tryNearbyStations: "या नजदीकी स्टेशन:",
    btnResetFilters: "फ़िल्टर रीसेट करें",
    chooseClassTitle: "अपनी यात्रा श्रेणी चुनें",
    chooseClassSubtitle: "इस ट्रेन के लिए सभी उपलब्ध डिब्बे और वास्तविक समय बर्थ स्थिति।",
    passengerDetailsTitle: "यात्रियों का विवरण",
    passengerDetailsSubtitle: "सरकारी पहचान पत्र के अनुसार जानकारी दर्ज करें।",
    trainName: "ट्रेन",
    route: "मार्ग एवं तिथि",
    classQuota: "श्रेणी एवं कोटा",
    farePerPerson: "प्रति व्यक्ति किराया",
    contactDetailsTitle: "ई-टिकट एवं एसएमएस के लिए संपर्क विवरण",
    labelMobile: "मोबाइल नंबर *",
    labelEmail: "ईमेल पता",
    contactNotice: "पीएनआर अपडेट और टिकट एसएमएस इसी मोबाइल नंबर पर भेजे जाएंगे।",
    continueToPayment: "भुगतान के लिए आगे बढ़ें →",
    paymentTitle: "समीक्षा एवं भुगतान",
    paymentSubtitle: "EasyRail प्रोटोटाइप के लिए 100% सुरक्षित सिम्युलेटेड भुगतान।",
    paymentFailed: "भुगतान विफल हुआ",
    bankDeclined: "आपके बैंक ने लेनदेन अस्वीकार कर दिया। (ERR_SIMULATED_DECLINE)",
    moneySafe: "आपके पैसे नहीं कटे हैं। कोई सीट आरक्षित नहीं हुई है।",
    tryAgain: "पुनः प्रयास करें",
    contactSupport: "सहायता एवं अक्सर पूछे जाने वाले प्रश्न",
    choosePaymentMethod: "भुगतान विधि चुनें",
    instantUPI: "लोकप्रिय यूपीआई ऐप्स से तुरंत भुगतान करें",
    orEnterUPI: "या यूपीआई आईडी (VPA) दर्ज करें",
    verify: "सत्यापित करें",
    cardNumber: "कार्ड नंबर",
    cardExpiry: "वैधता तिथि",
    cardCVV: "सीवीवी",
    cardHolder: "कार्ड पर नाम",
    cardSecurity: "आपके कार्ड का विवरण सुरक्षित है। यह केवल एक डेमो सिमुलेशन है।",
    popularBanks: "लोकप्रिय बैंक",
    allOtherBanks: "अन्य सभी बैंक",
    fareBreakdownTitle: "किराया विवरण",
    resvCharge: "आरक्षण शुल्क",
    superfastCharge: "सुपरफास्ट शुल्क",
    tatkalCharge: "तत्काल शुल्क",
    gst: "जीएसटी (5% एसी डिब्बे)",
    convenienceFee: "सुविधा शुल्क",
    totalPayable: "कुल देय राशि",
    simulatedNote: "EasyRail प्रोटोटाइप डेमो के लिए सभी शुल्क सिम्युलेटेड हैं।",
    demoFailCheck: "भुगतान विफलता का परीक्षण करें (डेमो मोड)",
    bookingConfirmedTitle: "बुकिंग कन्फर्म हो गई!",
    bookingConfirmedSubtitle: "आपकी यात्रा सफलतापूर्वक बुक हो गई है। सुखद यात्रा!",
    totalFarePaid: "कुल भुगतान किया गया किराया",
    printTicket: "टिकट प्रिंट करें",
    downloadTicket: "टिकट डाउनलोड करें",
    shareTicket: "टिकट साझा करें",
    bookAnother: "नई यात्रा बुक करें",
    myBookingsTitle: "मेरी बुकिंग",
    translateTicket: "टिकट अनुवाद करें (Sarvam AI)",
    bookNow: "अभी बुक करें →",
    runsDaily: "दैनिक चलती है",
    runsOnDays: "निर्धारित दिनों में चलती है",
    overnightTag: "+1 अगला दिन",
    catering: "⚡ ई-कैटरिंग",
    charging: "🔌 मोबाइल चार्जिंग",
    security: "🛡️ ऑन-बोर्ड सुरक्षा",
    statusAvailable: "उपलब्ध",
    statusRAC: "आरएसी",
    statusWL: "वेटलिस्ट",
    immediateConfirm: "त्वरित पुष्टि: भुगतान होते ही बर्थ तुरंत आवंटित और कन्फर्म कर दी जाएगी।",
    racNote: "आरएसी: आपको ट्रेन में यात्रा के लिए सीट मिलेगी। रद्दीकरण होने पर पूरा बर्थ मिलने की संभावना है।",
    wlNote: "वेटलिस्ट: आपकी बर्थ अभी पक्की नहीं है। कन्फर्म होने पर सूचित किया जाएगा। अपुष्ट रहने पर 100% रिफंड।",
    selectThisClass: "यह श्रेणी चुनें →",
    passenger: "यात्री",
    adultNotice: "वयस्क (5 वर्ष से अधिक)",
    fullNameLabel: "पूरा नाम *",
    fullNamePlaceholder: "सरकारी पहचान पत्र के अनुसार",
    ageLabel: "आयु *",
    genderLabel: "लिंग *",
    genderMale: "पुरुष",
    genderFemale: "महिला",
    genderOther: "अन्य",
    berthPrefLabel: "बर्थ प्राथमिकता",
    berthSubject: "(उपलब्धता पर निर्भर)",
    noPref: "कोई प्राथमिकता नहीं",
    lowerBerth: "निचली बर्थ",
    middleBerth: "मध्य बर्थ",
    upperBerth: "ऊपरी बर्थ",
    sideLowerBerth: "साइड लोअर",
    sideUpperBerth: "साइड अपर",
    valNameError: "कृपया मान्य पूरा नाम दर्ज करें।",
    valAgeError: "आयु 1 से 99 के बीच दर्ज करें।",
    valMobileError: "कृपया मान्य 10 अंकों का मोबाइल नंबर दर्ज करें।",
    ticketConfirmedBanner: "बुकिंग कन्फर्म हो गई!",
    ticketConfirmedSub: "आपकी यात्रा सफलतापूर्वक बुक हो गई है। सुखद और मंगलमय यात्रा!",
    waitlistBanner: "प्रतीक्षा सूची (वेटलिस्ट) टिकट जारी",
    waitlistSub: "आपका वेटलिस्ट टिकट जारी हो गया है। सीट कन्फर्म होने का विवरण एसएमएस द्वारा भेजा जाएगा।",
    verifyTicket: "टिकट सत्यापन",
    verifyTicketDesc: "डिजिटल हस्ताक्षर और पहचान सत्यापन स्थिति जांचने के लिए EasyRail ऐप से स्कैन करें।",
    pnrLabel: "पीएनआर नंबर",
    bookingTimeLabel: "बुकिंग का समय",
    txnIdLabel: "लेनदेन संख्या (Txn ID)",
    paymentSuccessLabel: "✓ भुगतान सफलतापूर्वक संपन्न",
    coachBerthLabel: "डिब्बा एवं बर्थ",
    baseFare: "मूल किराया",
    quickLangNotice: "भाषा बदल दी गई है:",
    tatkalBadgeTime: "⚡ प्रातः 10/11 बजे",
    tabUPI: "यूपीआई / क्यूआर",
    tabCard: "डेबिट / क्रेडिट कार्ड",
    tabNetBanking: "नेट बैंकिंग",
    tabWallets: "वॉलेट",
    confirmPassengerTitle: "यात्री विवरण की पुष्टि करें",
    irctcPolicyNote: "महत्वपूर्ण आईआरसीटीसी नियम:",
    irctcPolicyText: "टिकट कन्फर्म होने के बाद यात्री के नाम, आयु या लिंग में कोई बदलाव नहीं किया जा सकता। कृपया सरकारी पहचान पत्र से मिलान कर लें।",
    aadhaarVerifyNote: "आगे बढ़कर, आप पुष्टि करते हैं कि सभी यात्रियों के विवरण उनके आधार कार्ड या आधिकारिक पहचान पत्र से मेल खाते हैं।",
    btnEditDetails: "विवरण बदलें",
    btnProceedPay: "भुगतान के लिए आगे बढ़ें →",
    helpModalTitle: "EasyRail रेलवे मार्गदर्शिका एवं प्रश्नोत्तरी",
    tabCoachClasses: "कोच श्रेणियां (SL, 3A, 2A...)",
    tabSeatAvailability: "सीट उपलब्धता कोड",
    tabTatkalRules: "तत्काल समय एवं नियम",
    tabPaymentRefunds: "भुगतान एवं रिफंड",
    btnGotIt: "समझ गया",
    journeySummary: "यात्रा सारांश",
    noBookingsYet: "कोई बुकिंग उपलब्ध नहीं",
    noBookingsDesc: "आपकी बुक की गई यात्रा टिकट यहां आसानी से देखने और प्रिंट करने के लिए उपलब्ध होंगी।",
    stationWord: "स्टेशन",
    platformWord: "प्लेटफार्म",
    hoursWord: "घंटे",
    minsWord: "मिनट",
    dailyWord: "दैनिक"
  },
  te: {
    searchBtn: "రైళ్లు వెతకండి",
    from: "బయలుదేరే స్టేషన్",
    to: "గమ్యం స్టేషన్",
    tagline: "మీ ప్రయాణం, సులభతరం చేయబడింది.",
    navHome: "హోమ్",
    navBookings: "నా బుకింగ్స్",
    navHelp: "సహాయం",
    stepSearch: "వెతకండి",
    stepTrain: "రైలు ఎంచుకోండి",
    stepClass: "తరగతి ఎంచుకోండి",
    stepPassengers: "ప్రయాణీకులు",
    stepPayment: "చెల్లింపు",
    stepConfirm: "ధృవీకరణ",
    heroTitle: "మీ రైలు టిక్కెట్‌ను సులభంగా బుక్ చేసుకోండి",
    heroSubtitle: "గందరగోళం లేదు. సంక్లిష్టత లేదు. కేవలం సులభమైన బుకింగ్.",
    tabOneWay: "వన్ వే",
    tabRoundTrip: "రౌండ్ ట్రిప్",
    roundTripNotice: "(త్వరలో వస్తుంది)",
    labelFrom: "బయలుదేరే స్టేషన్",
    labelTo: "గమ్యం స్టేషన్",
    popular: "ప్రసిద్ధి చెందినవి:",
    labelDate: "ప్రయాణ తేదీ",
    today: "ఈరోజు",
    tomorrow: "రేపు",
    dayAfter: "ఎల్లుండి",
    labelPassengers: "ప్రయాణీకులు (1-6)",
    labelQuota: "ప్రయాణ కోటా",
    quotaGeneral: "జనరల్",
    quotaGeneralDesc: "ప్రామాణిక బుకింగ్",
    quotaLadies: "మహిళలు",
    quotaLadiesDesc: "మహిళల ప్రత్యేక కోటా",
    quotaSenior: "సీనియర్ సిటిజన్",
    quotaSeniorDesc: "దిగువ బెర్త్ ప్రాధాన్యత (60+)",
    quotaTatkal: "తత్కాల్",
    quotaTatkalDesc: "తక్షణ ప్రయాణం కోసం",
    btnSearchTrains: "రైళ్లు వెతకండి",
    helpSectionTitle: "మొదటిసారి టిక్కెట్ బుక్ చేస్తున్నారా? మేము మీకు సహాయం చేస్తాము.",
    helpSectionSubtitle: "రైల్వే టిక్కెట్లకు సంబంధించిన ముఖ్యమైన వివరాలు.",
    helpCard1Title: "SL / 2A / 3A అంటే ఏమిటి?",
    helpCard1Desc: "స్లీపర్ మరియు ఎయిర్ కండిషన్డ్ కోచ్‌ల తేడాలను వివరంగా తెలుసుకోండి.",
    helpCard2Title: "సీట్ల లభ్యత వివరాలు",
    helpCard2Desc: "కన్ఫర్మ్, ఆర్.ఎ.సి (RAC) మరియు వెయిట్‌లిస్ట్ (WL) అర్థాలు తెలుసుకోండి.",
    helpCard3Title: "చెల్లింపు భద్రత & రీఫండ్‌లు",
    helpCard3Desc: "వెయిట్‌లిస్ట్ రద్దయినప్పుడు తక్షణ రీఫండ్ మరియు భద్రతా విధానాలు.",
    learnMore: "మరింత తెలుసుకోండి →",
    modifySearch: "శోధన సవరించండి",
    filterAll: "అన్ని రైళ్లు",
    filterMorning: "ఉదయం (06:00 - 12:00)",
    filterEvening: "సాయంత్రం (18:00 - 24:00)",
    filterAC: "ఏసీ మాత్రమే",
    filterNonAC: "నాన్-ఏసీ",
    filterAvailable: "లభించేవి మాత్రమే",
    filterSuperfast: "సూపర్‌ఫాస్ట్",
    toggleNoTrainsDemo: "డెమో: 'రైళ్లు లేవు' స్థితి చూపించు",
    noTrainsTitle: "రైళ్లు ఏవీ కనుగొనబడలేదు",
    noTrainsDesc: "మీ శోధనకు తగిన రైళ్లు లేవు. దయచేసి ఇతర తేదీలు లేదా సమీప స్టేషన్లను చూడండి.",
    tryAlternateDates: "ప్రత్యామ్నాయ తేదీలు:",
    tryNearbyStations: "లేదా సమీప స్టేషన్లు:",
    btnResetFilters: "ఫిల్టర్లను రీసెట్ చేయండి",
    chooseClassTitle: "మీ ప్రయాణ తరగతిని ఎంచుకోండి",
    chooseClassSubtitle: "ఈ రైలులోని అన్ని కోచ్‌లు మరియు నిజ-సమయ బెర్త్ లభ్యత.",
    passengerDetailsTitle: "ప్రయాణీకుల వివరాలు",
    passengerDetailsSubtitle: "ప్రభుత్వ గుర్తింపు కార్డు ప్రకారం వివరాలను నమోదు చేయండి.",
    trainName: "రైలు",
    route: "మార్గం & తేదీ",
    classQuota: "తరగతి & కోటా",
    farePerPerson: "ఒక్కో ప్రయాణీకుడి ఛార్జీ",
    contactDetailsTitle: "ఈ-టికెట్ & ఎస్ఎంఎస్ కొరకు సంప్రదింపు వివరాలు",
    labelMobile: "మొబైల్ సంఖ్య *",
    labelEmail: "ఈమెయిల్ చిరునామా",
    contactNotice: "పి.ఎన్.ఆర్ అప్‌డేట్‌లు మరియు టికెట్ సమాచారం ఈ నంబర్‌కు పంపబడుతుంది.",
    continueToPayment: "చెల్లింపుకు కొనసాగండి →",
    paymentTitle: "సమీక్ష & చెల్లింపు",
    paymentSubtitle: "EasyRail ప్రోటోటైప్ కొరకు 100% సురక్షితమైన అనుకరణ చెల్లింపు.",
    paymentFailed: "చెల్లింపు విఫలమైంది",
    bankDeclined: "మీ బ్యాంక్ లావాదేవీని తిరస్కరించింది. (ERR_SIMULATED_DECLINE)",
    moneySafe: "మీ డబ్బు కట్ కాలేదు. ఎటువంటి సీటు బుక్ కాలేదు.",
    tryAgain: "మళ్ళీ ప్రయత్నించండి",
    contactSupport: "సహాయం & తరచుగా అడిగే ప్రశ్నలు",
    choosePaymentMethod: "చెల్లింపు పద్ధతిని ఎంచుకోండి",
    instantUPI: "ప్రసిద్ధ యూపీఐ యాప్‌లతో తక్షణ చెల్లింపు",
    orEnterUPI: "లేదా యూపీఐ ఐడీ నమోదు చేయండి",
    verify: "ధృవీకరించండి",
    cardNumber: "కార్డ్ నంబర్",
    cardExpiry: "చెల్లుబాటు తేదీ",
    cardCVV: "సీవీవీ",
    cardHolder: "కార్డుపై పేరు",
    cardSecurity: "మీ వివరాలు నిల్వ చేయబడవు. ఇది డెమో సిమ్యులేషన్ మాత్రమే.",
    popularBanks: "ప్రసిద్ధ బ్యాంకులు",
    allOtherBanks: "ఇతర బ్యాంకులు",
    fareBreakdownTitle: "ఛార్జీల వివరాలు",
    resvCharge: "రిజర్వేషన్ రుసుము",
    superfastCharge: "సూపర్‌ఫాస్ట్ ఛార్జ్",
    tatkalCharge: "తత్కాల్ ఛార్జ్",
    gst: "జీఎస్టీ (5% ఏసీ కోచ్‌లు)",
    convenienceFee: "సౌకర్య రుసుము",
    totalPayable: "మొత్తం చెల్లించవలసిన మొత్తం",
    simulatedNote: "EasyRail ప్రోటోటైప్ కోసం అన్ని ఛార్జీలు అనుకరించబడ్డాయి.",
    demoFailCheck: "చెల్లింపు వైఫల్యాన్ని అనుకరించండి (డెమో)",
    bookingConfirmedTitle: "బుకింగ్ నిర్ధారించబడింది!",
    bookingConfirmedSubtitle: "మీ ప్రయాణం విజయవంతంగా బుక్ చేయబడింది. శుభ ప్రయాణం!",
    totalFarePaid: "చెల్లించిన మొత్తం ఛార్జీ",
    printTicket: "టికెట్ ప్రింట్ చేయండి",
    downloadTicket: "టికెట్ డౌన్‌లోడ్ చేయండి",
    shareTicket: "టికెట్ షేర్ చేయండి",
    bookAnother: "మరొక ప్రయాణం బుక్ చేయండి",
    myBookingsTitle: "నా బుకింగ్స్",
    translateTicket: "టికెట్ అనువదించండి (Sarvam AI)",
    bookNow: "ఇప్పుడే బుక్ చేయండి →",
    runsDaily: "రోజూ నడుస్తుంది",
    runsOnDays: "ఎంచుకున్న రోజులలో నడుస్తుంది",
    overnightTag: "+1 మరుసటి రోజు",
    catering: "⚡ ఈ-కేటరింగ్",
    charging: "🔌 మొబైల్ ఛార్జింగ్",
    security: "🛡️ రైలులో భద్రత",
    statusAvailable: "లభ్యం",
    statusRAC: "ఆర్.ఎ.సి",
    statusWL: "వెయిట్‌లిస్ట్",
    immediateConfirm: "తక్షణ నిర్ధారణ: చెల్లింపు పూర్తయిన వెంటనే బెర్త్ కన్ఫర్మ్ చేయబడుతుంది.",
    racNote: "ఆర్.ఎ.సి: మీకు ప్రయాణించడానికి సీటు లభిస్తుంది. రద్దులు జరిగితే పూర్తి బెర్త్ కేటాయించబడుతుంది.",
    wlNote: "వెయిట్‌లిస్ట్: బెర్త్ ఇంకా ఖరారు కాలేదు. కన్ఫర్మ్ అయితే సమాచారం అందుతుంది. రద్దయితే 100% పూర్తి రీఫండ్.",
    selectThisClass: "ఈ తరగతిని ఎంచుకోండి →",
    passenger: "ప్రయాణీకుడు",
    adultNotice: "వయోజనుడు (5 సం.ల పైబడిన వారు)",
    fullNameLabel: "పూర్తి పేరు *",
    fullNamePlaceholder: "గుర్తింపు కార్డు ప్రకారం",
    ageLabel: "వయస్సు *",
    genderLabel: "లింగము *",
    genderMale: "పురుషుడు",
    genderFemale: "స్త్రీ",
    genderOther: "ఇతర",
    berthPrefLabel: "బెర్త్ ప్రాధాన్యత",
    berthSubject: "(లభ్యతపై ఆధారపడి ఉంటుంది)",
    noPref: "ప్రాధాన్యత లేదు",
    lowerBerth: "దిగువ బెర్త్",
    middleBerth: "మధ్య బెర్త్",
    upperBerth: "పై బెర్త్",
    sideLowerBerth: "సైడ్ లోయర్",
    sideUpperBerth: "సైడ్ అప్పర్",
    valNameError: "దయచేసి సరైన పూర్తి పేరును నమోదు చేయండి.",
    valAgeError: "వయస్సు 1-99 నమోదు చేయండి.",
    valMobileError: "దయచేసి సరైన 10 అంకెల మొబైల్ నంబర్‌ను నమోదు చేయండి.",
    ticketConfirmedBanner: "బుకింగ్ విజయవంతంగా నిర్ధారించబడింది!",
    ticketConfirmedSub: "మీ ప్రయాణం విజయవంతంగా బుక్ చేయబడింది. శుభ ప్రయాణం!",
    waitlistBanner: "వెయిట్‌లిస్ట్ టిక్కెట్ జారీ చేయబడింది",
    waitlistSub: "మీ వెయిట్‌లిస్ట్ టిక్కెట్ రూపొందించబడింది. సీటు కన్ఫర్మేషన్ వివరాలు ఎస్ఎంఎస్ ద్వారా పంపబడతాయి.",
    verifyTicket: "టికెట్ ధృవీకరణ",
    verifyTicketDesc: "డిజిటల్ సంతకం మరియు గుర్తింపు ధృవీకరణ తనిఖీ చేయడానికి EasyRail యాప్‌తో స్కాన్ చేయండి.",
    pnrLabel: "పి.ఎన్.ఆర్ సంఖ్య",
    bookingTimeLabel: "బుకింగ్ సమయం",
    txnIdLabel: "లావాదేవీ ఐడీ (Txn ID)",
    paymentSuccessLabel: "✓ చెల్లింపు నిర్ధారించబడింది",
    coachBerthLabel: "కోచ్ & బెర్త్",
    baseFare: "ప్రాథమిక ఛార్జీ",
    quickLangNotice: "భాష మార్చబడింది:",
    tatkalBadgeTime: "⚡ ఉదయం 10/11 గం.",
    tabUPI: "యూపీఐ / క్యూఆర్",
    tabCard: "డెబిట్ / క్రెడిట్ కార్డు",
    tabNetBanking: "నెట్ బ్యాంకింగ్",
    tabWallets: "వ్యాలెట్లు",
    confirmPassengerTitle: "ప్రయాణీకుల వివరాలను నిర్ధారించండి",
    irctcPolicyNote: "ముఖ్యమైన ఐఆర్సీటీసీ నిబంధన:",
    irctcPolicyText: "టికెట్ కన్ఫర్మ్ అయిన తర్వాత ప్రయాణీకుల పేరు, వయస్సు లేదా లింగంలో ఎలాంటి మార్పులు అనుమతించబడవు. దయచేసి వివరాలను సరిచూసుకోండి.",
    aadhaarVerifyNote: "కొనసాగడం ద్వారా, ప్రయాణీకులందరి వివరాలు వారి ఆధార్ లేదా ప్రభుత్వ గుర్తింపు కార్డుతో సరిపోలుతున్నాయని మీరు ధృవీకరిస్తున్నారు.",
    btnEditDetails: "వివరాలను సవరించండి",
    btnProceedPay: "చెల్లింపుకు కొనసాగండి →",
    helpModalTitle: "EasyRail రైల్వే గైడ్ & తరచుగా అడిగే ప్రశ్నలు",
    tabCoachClasses: "కోచ్ తరగతులు (SL, 3A, 2A...)",
    tabSeatAvailability: "సీట్ల లభ్యత కోడ్‌లు",
    tabTatkalRules: "తత్కాల్ వేళలు & నిబంధనలు",
    tabPaymentRefunds: "చెల్లింపు & రీఫండ్‌లు",
    btnGotIt: "అర్థమైంది",
    journeySummary: "ప్రయాణ సారాంశం",
    noBookingsYet: "ఇంకా ఎటువంటి బుకింగ్స్ లేవు",
    noBookingsDesc: "మీరు బుక్ చేసుకున్న ప్రయాణ టిక్కెట్లు ఇక్కడ కనిపిస్తాయి.",
    stationWord: "స్టేషన్",
    platformWord: "ప్లాట్‌ఫారమ్",
    hoursWord: "గం.",
    minsWord: "నిమి.",
    dailyWord: "రోజూ"
  }
};

// --- 6. Core Navigation & Utilities ---
function showScreen(screenId) {
  appState.currentScreen = screenId;
  
  // Hide all screens
  document.querySelectorAll(".screen").forEach(el => {
    el.classList.remove("active");
  });
  
  // Show target screen
  const target = document.getElementById(`screen-${screenId}`);
  if (target) {
    target.classList.add("active");
  }
  
  // Update Progress Stepper visibility & nodes
  const stepperSec = document.getElementById("progress-stepper-section");
  const stepperFill = document.getElementById("stepper-progress-fill");
  
  if (screenId === 1) {
    if (stepperSec) stepperSec.style.display = "none";
  } else {
    if (stepperSec) stepperSec.style.display = "block";
    
    const steps = [1, 2, 3, 4, 5, 6];
    steps.forEach(step => {
      const node = document.getElementById(`step-node-${step}`);
      if (node) {
        node.classList.remove("active", "completed");
        const circle = node.querySelector(".step-circle");
        if (step < screenId) {
          node.classList.add("completed");
          if (circle) circle.innerHTML = "✓";
        } else if (step === screenId) {
          node.classList.add("active");
          if (circle) circle.textContent = step;
        } else {
          if (circle) circle.textContent = step;
        }
      }
    });
    
    if (stepperFill) {
      const progressPercent = ((screenId - 1) / 5) * 100;
      stepperFill.style.width = `${progressPercent}%`;
    }
  }
  
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function formatDate(d) {
  if (!d) return "22 Nov 2026";
  const dateObj = new Date(d + "T00:00:00");
  const options = { day: "numeric", month: "short", year: "numeric" };
  return dateObj.toLocaleDateString("en-IN", options);
}

function getTomorrowDateStr() {
  const d = new Date();
  d.setDate(d.getDate() + 1);
  const yyyy = d.getFullYear();
  const mm = String(d.getMonth() + 1).padStart(2, "0");
  const dd = String(d.getDate()).padStart(2, "0");
  return `${yyyy}-${mm}-${dd}`;
}

function isTomorrow(dateStr) {
  if (!dateStr) return false;
  return dateStr === getTomorrowDateStr();
}

function formatCurrency(n) {
  return "₹" + Number(n).toLocaleString("en-IN");
}

function generatePNR() {
  return Math.floor(1000000000 + Math.random() * 9000000000).toString();
}

function translate(key) {
  return (i18n[appState.language] && i18n[appState.language][key]) || i18n.en[key] || key;
}

// --- 5.1 Sarvam AI Deep Context Translation Engine ---
const SarvamAI = {
  apiEndpoint: "https://api.sarvam.ai/translate",
  model: "mayura:v1",
  storageKey: "sarvam_api_key",
  cacheStorageKey: "sarvam_trans_cache_v2",
  cache: {},

  init() {
    try {
      const saved = localStorage.getItem(this.cacheStorageKey);
      if (saved) {
        this.cache = JSON.parse(saved);
      }
    } catch (e) {
      this.cache = {};
    }
    this.updateStatusBadge();
  },

  getApiKey() {
    return localStorage.getItem(this.storageKey) || "";
  },

  setApiKey(key) {
    if (key && key.trim()) {
      localStorage.setItem(this.storageKey, key.trim());
    } else {
      localStorage.removeItem(this.storageKey);
    }
    this.updateStatusBadge();
  },

  updateStatusBadge() {
    const badge = document.getElementById("sarvam-api-status-badge");
    const key = this.getApiKey();
    if (!badge) return;
    if (key) {
      badge.innerHTML = `<span class="status-dot green"></span><span>Live Sarvam AI API (${this.model})</span>`;
    } else {
      badge.innerHTML = `<span class="status-dot green"></span><span>Deep Context Engine Active</span>`;
    }
  },

  detectFormality(text, lang) {
    const lower = (text || "").toLowerCase();
    if (lang === "hi-IN" || lang === "hi") {
      if (text.includes("आप") || text.includes("कृपया") || text.includes("जी")) return "formal";
      if (text.includes("तू") || text.includes("तुम")) return "modern-colloquial";
    }
    if (lang === "te-IN" || lang === "te") {
      if (text.includes("మీరు") || text.includes("దయచేసి") || text.includes("గారు")) return "formal";
      if (text.includes("నువ్వు") || text.includes("నీవు")) return "modern-colloquial";
    }
    if (lang === "en-IN" || lang === "en") {
      if (lower.includes("please") || lower.includes("kindly") || lower.includes("sir") || lower.includes("madam")) return "formal";
      if (lower.includes("hey") || lower.includes("wanna") || lower.includes("gonna")) return "modern-colloquial";
    }
    return "formal";
  },

  detectGender(text, lang) {
    const lower = (text || "").toLowerCase();
    if (lower.includes("mr.") || lower.includes("sir") || lower.includes("male") || lower.includes("boy") || lower.includes("శ్రీ") || lower.includes("श्री")) return "Male";
    if (lower.includes("mrs.") || lower.includes("ms.") || lower.includes("madam") || lower.includes("female") || lower.includes("girl") || lower.includes("శ్రీమతి") || lower.includes("श्रीमती")) return "Female";
    return "None";
  },

  detectLanguage(text) {
    for (let i = 0; i < text.length; i++) {
      const code = text.charCodeAt(i);
      if (code >= 0x0900 && code <= 0x097F) return "hi-IN";
      if (code >= 0x0C00 && code <= 0x0C7F) return "te-IN";
    }
    return "en-IN";
  },

  async translate({ input, sourceLang = "auto", targetLang = "te-IN", mode = "formal", speakerGender = "None", numeralsFormat = "international" }) {
    if (!input || !input.trim()) return "";
    const clean = input.trim();

    let src = sourceLang === "auto" ? this.detectLanguage(clean) : sourceLang;
    if (src === "en") src = "en-IN";
    if (src === "hi") src = "hi-IN";
    if (src === "te") src = "te-IN";

    let tgt = targetLang;
    if (tgt === "en") tgt = "en-IN";
    if (tgt === "hi") tgt = "hi-IN";
    if (tgt === "te") tgt = "te-IN";

    if (src === tgt) return clean;

    const cacheKey = `${src}->${tgt}::${mode}::${speakerGender}::${clean}`;
    if (this.cache[cacheKey]) {
      return this.cache[cacheKey];
    }

    const key = this.getApiKey();
    if (key) {
      try {
        const payload = {
          input: clean,
          source_language_code: src,
          target_language_code: tgt,
          model: this.model,
          mode: mode || "formal",
          numerals_format: numeralsFormat || "international"
        };
        if (speakerGender && speakerGender !== "None") {
          payload.speaker_gender = speakerGender;
        }

        const res = await fetch(this.apiEndpoint, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "api-subscription-key": key
          },
          body: JSON.stringify(payload)
        });

        if (res.ok) {
          const data = await res.json();
          if (data && data.translated_text) {
            this.cache[cacheKey] = data.translated_text;
            try { localStorage.setItem(this.cacheStorageKey, JSON.stringify(this.cache)); } catch(e){}
            return data.translated_text;
          }
        }
      } catch (err) {
        console.warn("Live Sarvam AI API call failed, falling back to context engine:", err);
      }
    }

    // Deep context-aware fallback
    const result = this.getContextualFallback(clean, tgt, src);
    this.cache[cacheKey] = result;
    try { localStorage.setItem(this.cacheStorageKey, JSON.stringify(this.cache)); } catch(e){}
    return result;
  },

  getContextualFallback(text, targetLang, sourceLang) {
    const tgt = targetLang.split("-")[0];
    const corpus = {
      "Book your train ticket easily": {
        hi: "अपनी ट्रेन टिकट आसानी से बुक करें",
        te: "మీ రైలు టిక్కెట్‌ను సులభంగా బుక్ చేసుకోండి",
        en: "Book your train ticket easily"
      },
      "No confusion. No jargon. Just simple booking.": {
        hi: "कोई भ्रम नहीं। कोई जटिलता नहीं। बस सरल बुकिंग।",
        te: "ఎటువంటి గందరగోళం లేకుండా సులభంగా టికెట్ బుక్ చేసుకోండి.",
        en: "No confusion. No jargon. Just simple booking."
      },
      "Booking Confirmed!": {
        hi: "बुकिंग सफलतापूर्वक कन्फर्म हुई!",
        te: "బుకింగ్ విజయవంతంగా నిర్ధారించబడింది!",
        en: "Booking Confirmed!"
      },
      "Your journey is booked. Have a great trip!": {
        hi: "आपकी यात्रा बुक हो गई है। सुखद और मंगलमय यात्रा!",
        te: "మీ ప్రయాణం విజయవంతంగా బుక్ చేయబడింది. శుభ ప్రయాణం!",
        en: "Your journey is booked. Have a great trip!"
      },
      "Waitlist Ticket Issued": {
        hi: "प्रतीक्षा सूची (वेटलिस्ट) टिकट जारी किया गया",
        te: "వెయిట్‌లిస్ట్ టిక్కెట్ జారీ చేయబడింది",
        en: "Waitlist Ticket Issued"
      },
      "Your waitlisted ticket has been generated. Seat confirmation updates will be sent via SMS.": {
        hi: "आपका प्रतीक्षा सूची टिकट तैयार हो गया है। सीट कन्फर्म होने का विवरण एसएमएस द्वारा भेजा जाएगा।",
        te: "మీ వెయిట్‌లిస్ట్ టిక్కెట్ రూపొందించబడింది. సీటు కన్ఫర్మేషన్ వివరాలు ఎస్ఎంఎస్ ద్వారా పంపబడతాయి.",
        en: "Your waitlisted ticket has been generated. Seat confirmation updates will be sent via SMS."
      },
      "Tatkal quota tickets are subject to full cancellation charges after chart preparation.": {
        hi: "चार्ट तैयार होने के पश्चात तत्काल कोटा टिकट रद्द करने पर कोई रिफंड नहीं दिया जाता है।",
        te: "చార్ట్ తయారీ పూర్తయిన తర్వాత తత్కాల్ కోటా టిక్కెట్లను రద్దు చేస్తే ఎటువంటి రీఫండ్ లభించదు.",
        en: "Tatkal quota tickets are subject to full cancellation charges after chart preparation."
      },
      "Please carry original government-issued photo ID for IRCTC ticket verification.": {
        hi: "कृपया यात्रा के दौरान IRCTC सत्यापन हेतु मूल सरकारी फोटो पहचान पत्र साथ रखें।",
        te: "దయచేసి ప్రయాణంలో IRCTC టికెట్ తనిఖీ కొరకు అసలైన ప్రభుత్వ గుర్తింపు కార్డు వెంట ఉంచుకోండి.",
        en: "Please carry original government-issued photo ID for IRCTC ticket verification."
      },
      "RAC (Reservation Against Cancellation): You are guaranteed a seat to travel on the train!": {
        hi: "आरएसी (रद्द के विरुद्ध आरक्षण): आपको ट्रेन में यात्रा के लिए निश्चित सीट प्रदान की जाती है!",
        te: "ఆర్.ఎ.సి (రద్దుకు వ్యతిరేకంగా రిజర్వేషన్): మీకు రైలులో ప్రయాణించడానికి సీటు ఖచ్చితంగా లభిస్తుంది!",
        en: "RAC (Reservation Against Cancellation): You are guaranteed a seat to travel on the train!"
      },
      "Immediate Confirmation: Berths are available for immediate confirmation upon payment.": {
        hi: "त्वरित पुष्टि: भुगतान होते ही बर्थ तुरंत आवंटित और कन्फर्म कर दी जाएगी।",
        te: "తక్షణ నిర్ధారణ: చెల్లింపు పూర్తయిన వెంటనే బెర్త్ కన్ఫర్మ్ చేయబడుతుంది.",
        en: "Immediate Confirmation: Berths are available for immediate confirmation upon payment."
      },
      "Instant refunds for unconfirmed waitlisted tickets will be credited to source payment method.": {
        hi: "अपुष्ट प्रतीक्षा सूची टिकटों का त्वरित रिफंड आपके मूल बैंक खाते में स्वतः वापस जमा हो जाएगा।",
        te: "కన్ఫర్మ్ కాని వెయిట్‌లిస్ట్ టిక్కెట్ల తక్షణ రీఫండ్ మీ అసలు చెల్లింపు ఖాతాకు స్వయంచాలకంగా జమ చేయబడుతుంది.",
        en: "Instant refunds for unconfirmed waitlisted tickets will be credited to source payment method."
      }
    };

    if (corpus[text] && corpus[text][tgt]) {
      return corpus[text][tgt];
    }

    if (text.includes("Kerala Express") || text.includes("Visakha Express") || text.includes("Platform")) {
      if (tgt === "te") return "మీ రైలు 12626 కేరళ ఎక్స్‌ప్రెస్ సమయానికి నడుస్తోంది. ప్లాట్‌ఫారమ్ 3 వద్దకు చేరుకుంటుంది. కోచ్ B2, బెర్త్ 34 (దిగువ బెర్త్).";
      if (tgt === "hi") return "आपकी ट्रेन 12626 केरल एक्सप्रेस समय पर चल रही है। प्लेटफार्म नंबर 3 पर आएगी। कोच B2, बर्थ 34 (निचली बर्थ)।";
      return "Your train 12626 Kerala Express is running on time. Arriving at Platform 3. Coach B2, Berth 34 (Lower).";
    }

    if (text.includes("Tatkal") || text.includes("tatkal")) {
      if (tgt === "te") return "తత్కాల్ కోటా టిక్కెట్లు ప్రయాణ తేదీకి 1 రోజు ముందు ఉదయం 10 గంటలకు (ఏసీ) మరియు ఉదయం 11 గంటలకు (నాన్-ఏసీ) ప్రారంభమవుతాయి. చార్ట్ తయారీ తర్వాత రద్దు చేస్తే రీఫండ్ లభించదు.";
      if (tgt === "hi") return "तत्काल कोटा टिकट यात्रा की तिथि से 1 दिन पूर्व प्रातः 10:00 बजे (एसी) एवं 11:00 बजे (नॉन-एसी) खुलते हैं। चार्ट बनने के पश्चात रद्द करने पर कोई रिफंड देय नहीं होता है।";
      return "Tatkal quota tickets open exactly 1 day prior to departure at 10:00 AM (AC) and 11:00 AM (Non-AC). No refund on cancellation of confirmed Tatkal tickets.";
    }

    if (text.includes("RAC") || text.includes("Waitlist") || text.includes("WL")) {
      if (tgt === "te") return "ఆర్.ఎ.సి (RAC) అంటే రైలులో ప్రయాణించడానికి సీటు ఖచ్చితంగా లభిస్తుంది. వెయిట్‌లిస్ట్ (WL) లో సీటు కేటాయించబడదు; చార్ట్ తయారీ సమయానికి ఖాళీలు ఏర్పడితే కన్ఫర్మ్ అవుతుంది.";
      if (tgt === "hi") return "आरएसी (RAC) में आपको यात्रा के लिए निश्चित सीट मिलती है। वेटलिस्ट (WL) में अभी कोई सीट आवंटित नहीं है; चार्ट बनने पर सीट खाली होने पर टिकट कन्फर्म हो जाता है।";
      return "RAC guarantees a travel seat on the train. Waitlist (WL) does not allot a berth yet; it upgrades to RAC or Confirmed if cancellations occur before charting.";
    }

    if (text.includes("Senior") || text.includes("Lower Berth") || text.includes("60+")) {
      if (tgt === "te") return "60 ఏళ్లు పైబడిన పురుషులు మరియు 45 ఏళ్లు పైబడిన ఒంటరి మహిళలకు భారతీయ రైల్వే నిబంధనల ప్రకారం స్వయంచాలకంగా దిగువ బెర్త్ (Lower Berth) ప్రాధాన్యత లభిస్తుంది.";
      if (tgt === "hi") return "60 वर्ष से अधिक आयु के पुरुषों एवं 45 वर्ष से अधिक आयु की एकल महिला यात्रियों को भारतीय रेल नियमानुसार स्वतः निचली बर्थ (लोअर बर्थ) प्राथमिकता दी जाती है।";
      return "Male passengers aged 60+ and solo female passengers aged 45+ are automatically given lower berth priority as per Indian Railways quota rules.";
    }

    if (text.includes("Helpline") || text.includes("Security") || text.includes("139")) {
      if (tgt === "te") return "భారతీయ రైల్వే అత్యవసర ప్రయాణీకుల సహాయం, భద్రత మరియు పి.ఎన్.ఆర్ సమాచారం కొరకు 24x7 ఏకీకృత హెల్ప్‌లైన్ సంఖ్య 139 అందుబాటులో ఉంటుంది.";
      if (tgt === "hi") return "भारतीय रेल आपातकालीन सहायता, सुरक्षा, चिकित्सा एवं पीएनआर पूछताछ हेतु 24x7 एकीकृत यात्री हेल्पलाइन नंबर 139 संचालित करती है।";
      return "Indian Railways operates the 24x7 unified passenger emergency helpline 139 for security, medical help, and real-time train status.";
    }

    return text;
  }
};

// --- 5.2 Domain Terminology & Localization Helpers ---
const localizedTrainNames = {
  "Visakha Express":    { hi: "विशाखा एक्सप्रेस",      te: "విశాఖ ఎక్స్‌ప్రెస్" },
  "East Coast Express": { hi: "ईस्ट कोस्ट एक्सप्रेस",  te: "ఈస్ట్ కోస్ట్ ఎక్స్‌ప్రెస్" },
  "Godavari SF Express":{ hi: "गोदावरी सुपरफास्ट एक्सप्रेस", te: "గోదావరి సూపర్‌ఫాస్ట్ ఎక్స్‌ప్రెస్" },
  "Godavari Express":   { hi: "गोदावरी एक्सप्रेस",     te: "గోదావరి ఎక్స్‌ప్రెస్" },
  "Konark Express":     { hi: "कोणार्क एक्सप्रेस",     te: "కోణార్క్ ఎక్స్‌ప్రెస్" },
  "Tatkal Special":     { hi: "तत्काल स्पेशल",          te: "తత్కాల్ స్పెషల్" },
  "Vande Bharat Express":{ hi: "वंदे भारत एक्सप्रेस",  te: "వందే భారత్ ఎక్స్‌ప్రెస్" },
  "Garib Rath Express": { hi: "गरीब रथ एक्सप्रेस",     te: "గరీబ్ రథ్ ఎక్స్‌ప్రెస్" },
  "Jan Shatabdi":       { hi: "जन शताब्दी एक्सप्रेस",  te: "జన శతాబ్ది ఎక్స్‌ప్రెస్" },
  "Falaknuma Express":  { hi: "फलकनुमा एक्सप्रेस",     te: "ఫలక్‌నుమా ఎక్స్‌ప్రెస్" },
  "Prasanthi Express":  { hi: "प्रशांति एक्सप्रेस",    te: "ప్రశాంతి ఎక్స్‌ప్రెస్" },
  "Kerala Express":     { hi: "केरल एक्सप्रेस",         te: "కేరళ ఎక్స్‌ప్రెస్" },
  "Telangana Express":  { hi: "तेलंगाना एक्सप्रेस",    te: "తెలంగాణ ఎక్స్‌ప్రెస్" },
  "Charminar Express":  { hi: "चारमीनार एक्सप्रेस",    te: "చార్మినార్ ఎక్స్‌ప్రెస్" },
  "Bengaluru Rajdhani": { hi: "बेंगलुरु राजधानी",       te: "బెంగళూరు రాజధాని" }
};

function getLocalizedTrainName(name) {
  if (appState.language === "en" || !name) return name;
  const match = localizedTrainNames[name];
  if (match && match[appState.language]) {
    return match[appState.language];
  }
  return name;
}

const localizedStationNames = {
  VSKP: { en: "Visakhapatnam (VSKP)", hi: "विशाखापट्टनम (VSKP)", te: "విశాఖపట్నం (VSKP)" },
  SC:   { en: "Secunderabad (SC)",    hi: "सिकंदराबाद (SC)",      te: "సికింద్రాబాద్ (SC)" },
  BZA:  { en: "Vijayawada (BZA)",    hi: "विजयवाड़ा (BZA)",      te: "విజయవాడ (BZA)" },
  MAS:  { en: "Chennai Central (MAS)", hi: "चेन्नई सेंट्रल (MAS)", te: "చెన్నై సెంట్రల్ (MAS)" },
  NDLS: { en: "New Delhi (NDLS)",    hi: "नई दिल्ली (NDLS)",     te: "న్యూ ఢిల్లీ (NDLS)" },
  SBC:  { en: "Bengaluru City (SBC)", hi: "बेंगलुरु सिटी (SBC)", te: "బెంగళూరు సిటీ (SBC)" },
  HWH:  { en: "Howrah (HWH)",        hi: "हावड़ा (HWH)",          te: "హౌరా (HWH)" },
  CSMT: { en: "Mumbai CSMT (CSMT)",  hi: "मुंबई छत्रपति शिवाजी महाराज टर्मिनस (CSMT)", te: "ముంబై సీఎస్‌ఎంటీ (CSMT)" },
  PUNE: { en: "Pune (PUNE)",         hi: "पुणे (PUNE)",           te: "పూణే (PUNE)" },
  ADI:  { en: "Ahmedabad (ADI)",     hi: "अहमदाबाद (ADI)",       te: "అహ్మదాబాద్ (ADI)" },
  PNBE: { en: "Patna (PNBE)",        hi: "पटना (PNBE)",           te: "పాట్నా (PNBE)" },
  JP:   { en: "Jaipur (JP)",         hi: "जयपुर (JP)",            te: "జైపూర్ (JP)" },
  HYB:  { en: "Hyderabad (HYB)",     hi: "हैदराबाद (HYB)",       te: "హైదరాబాద్ (HYB)" },
  GHY:  { en: "Guwahati (GHY)",      hi: "गुवाहाटी (GHY)",       te: "గువాహటి (GHY)" },
  TVC:  { en: "Trivandrum (TVC)",    hi: "तिरुवनंतपुरम (TVC)",   te: "తిరువనంతపురం (TVC)" },
  DVD:  { en: "Duvvada (DVD)",       hi: "दुव्वाडा (DVD)",        te: "దువ్వాడ (DVD)" }
};

function getLocalizedStationName(code) {
  if (!code) return "";
  const entry = localizedStationNames[code];
  if (entry && entry[appState.language]) {
    return entry[appState.language];
  }
  return code;
}

// Localize duration strings like "8h 10m" -> "8 घंटे 10 मिनट" / "8 గం. 10 నిమి."
function formatDuration(durationStr) {
  if (!durationStr || appState.language === "en") return durationStr;
  const match = durationStr.match(/(\d+)h\s*(\d+)m/);
  if (!match) return durationStr;
  const h = match[1], m = match[2];
  if (appState.language === "hi") return `${h} घंटे ${m} मिनट`;
  if (appState.language === "te") return `${h} గం. ${m} నిమి.`;
  return durationStr;
}

// Return localized 1-letter abbreviations for M T W T F S S
function getLocalizedDayLabels() {
  if (appState.language === "hi") return ["सो","मं","बु","गु","शु","श","र"];
  if (appState.language === "te") return ["సో","మం","బు","గు","శు","శ","ఆ"];
  return ["M","T","W","T","F","S","S"];
}

function getLocalizedBerthType(berthStr) {
  if (!berthStr) return "";
  if (appState.language === "hi") {
    if (berthStr.includes("Lower")) return "निचली (Lower)";
    if (berthStr.includes("Middle")) return "मध्य (Middle)";
    if (berthStr.includes("Upper")) return "ऊपरी (Upper)";
    if (berthStr.includes("Side Lower")) return "साइड लोअर";
    if (berthStr.includes("Side Upper")) return "साइड अपर";
    if (berthStr.includes("Chair")) return "चेयर कार सीट";
  }
  if (appState.language === "te") {
    if (berthStr.includes("Lower")) return "దిగువ (Lower)";
    if (berthStr.includes("Middle")) return "మధ్య (Middle)";
    if (berthStr.includes("Upper")) return "పై బెర్త్ (Upper)";
    if (berthStr.includes("Side Lower")) return "సైడ్ లోయర్";
    if (berthStr.includes("Side Upper")) return "సైడ్ అప్పర్";
    if (berthStr.includes("Chair")) return "చైర్ కార్ సీటు";
  }
  return berthStr;
}

function getLocalizedQuota(quotaStr) {
  const map = {
    General: { en: "General", hi: "सामान्य कोटा", te: "సాధారణ కోటా" },
    Ladies: { en: "Ladies", hi: "महिला कोटा", te: "మహిళల కోటా" },
    "Senior Citizen": { en: "Senior Citizen", hi: "वरिष्ठ नागरिक कोटा", te: "సీనియర్ సిటిజన్ కోటా" },
    Tatkal: { en: "Tatkal", hi: "तत्काल कोटा", te: "తత్కాల్ కోటా" }
  };
  if (map[quotaStr] && map[quotaStr][appState.language]) {
    return map[quotaStr][appState.language];
  }
  return quotaStr;
}

// Build localized journey summary meta string
function buildSummaryMeta(dateStr, count, quota) {
  const lang = appState.language;
  const d = formatDate(dateStr);
  const q = getLocalizedQuota(quota);
  if (lang === "hi") {
    return `${d} · ${count} यात्री · ${q}`;
  }
  if (lang === "te") {
    return `${d} · ${count} ప్రయాణీకులు · ${q}`;
  }
  return `${d} · ${count} Passenger(s) · ${q}`;
}

// Build localized route string "VSKP → SC"
function buildSummaryRoute(fromCode, toCode) {
  const arrow = appState.language === "hi" ? " → " : " → ";
  return `${fromCode}${arrow}${toCode}`;
}

function translateTrainType(type) {
  if (appState.language === "hi") {
    if (type === "Superfast") return "सुपरफास्ट";
    if (type === "Express") return "एक्सप्रेस";
    if (type === "Tatkal") return "तत्काल";
  }
  if (appState.language === "te") {
    if (type === "Superfast") return "సూపర్‌ఫాస్ట్";
    if (type === "Express") return "ఎక్స్‌ప్రెస్";
    if (type === "Tatkal") return "తత్కాల్";
  }
  return type;
}

function getLocalizedClassInfo(code, fallbackName) {
  const base = classDescriptions[code] || {
    fullName: fallbackName || code,
    badge: "Standard",
    desc: "Comfortable railway coach accommodation.",
    icon: "🛌"
  };

  if (appState.language === "hi") {
    const hiMap = {
      SL: { fullName: "स्लीपर क्लास", badge: "गैर-एसी शयनयान", desc: "स्लीपर क्लास — खुली खिड़कियों और 3-टियर बर्थ वाला गैर-वातानुकूलित कोच। किफायती और हवादार।" },
      "3A": { fullName: "एसी 3 टियर", badge: "वातानुकूलित", desc: "एसी 3 टियर — वातानुकूलित कोच जिसमें प्रति बे 3 बर्थ होती हैं। चादर और कंबल उपलब्ध।" },
      "2A": { fullName: "एसी 2 टियर", badge: "अधिक गोपनीयता", desc: "एसी 2 टियर — वातानुकूलित कोच जिसमें प्रति बे 2 बर्थ होती हैं। अधिक चौड़े बर्थ और पर्दे।" },
      "1A": { fullName: "एसी प्रथम श्रेणी", badge: "प्रीमियम केबिन", desc: "एसी प्रथम श्रेणी — 2 या 4 बर्थ वाला निजी कूप। सर्वोत्तम आरामदायक यात्रा अनुभव।" },
      CC: { fullName: "एसी चेयर कार", badge: "रिक्लाइनिंग सीट", desc: "चेयर कार — आरामदायक पुश-बैक सीटें। 5 घंटे से कम की दिन की यात्रा के लिए सबसे उपयुक्त।" }
    };
    if (hiMap[code]) {
      return { ...base, fullName: hiMap[code].fullName, badge: hiMap[code].badge, desc: hiMap[code].desc };
    }
  }

  if (appState.language === "te") {
    const teMap = {
      SL: { fullName: "స్లీపర్ క్లాస్", badge: "నాన్-ఏసీ కోచ్", desc: "స్లీపర్ క్లాస్ — నాన్-ఏసీ కోచ్, 3-టైర్ బెర్తులు మరియు విశాలమైన కిటికీలు. బడ్జెట్ ప్రయాణానికి అనుకూలం." },
      "3A": { fullName: "ఏసీ 3 టైర్", badge: "ఎయిర్ కండిషన్డ్", desc: "ఏసీ 3 టైర్ — ఎయిర్ కండిషన్డ్ కోచ్, బే కి 3 బెర్తులు. ప్రయాణంలో దుప్పట్లు మరియు బెడ్‌షీట్లు అందించబడతాయి." },
      "2A": { fullName: "ఏసీ 2 టైర్", badge: "మరింత ప్రశాంతత", desc: "ఏసీ 2 టైర్ — ఎయిర్ కండిషన్డ్ కోచ్, బే కి 2 బెర్తులు మాత్రమే. విస్తృత బెర్తులు మరియు కర్టెన్లు." },
      "1A": { fullName: "ఏసీ ఫస్ట్ క్లాస్", badge: "ప్రీమియం క్యాబిన్", desc: "ఏసీ ఫస్ట్ క్లాస్ — 2 లేదా 4 బెర్తుల ప్రైవేట్ కూపే. అత్యున్నత లగ్జరీ ప్రయాణ అనుభవం." },
      CC: { fullName: "ఏసీ చైర్ కార్", badge: "పుష్-బ్యాక్ సీట్లు", desc: "చైర్ కార్ — సౌకర్యవంతమైన పుష్-బ్యాక్ సీట్లు. 5 గంటల లోపు పగటి ప్రయాణాలకు అత్యుత్తమం." }
    };
    if (teMap[code]) {
      return { ...base, fullName: teMap[code].fullName, badge: teMap[code].badge, desc: teMap[code].desc };
    }
  }

  return base;
}

function applyTranslations() {
  // 1. Text content with data-i18n
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    const text = translate(key);
    if (text) {
      el.textContent = text;
    }
  });

  // 2. Placeholders with data-i18n-placeholder
  document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
    const key = el.getAttribute("data-i18n-placeholder");
    const text = translate(key);
    if (text) {
      el.setAttribute("placeholder", text);
    }
  });

  // 3. Current Language Label
  const langLabelMap = { en: "EN", hi: "हि", te: "తె" };
  const currentLangLabel = document.getElementById("current-lang-label");
  if (currentLangLabel) {
    currentLangLabel.textContent = langLabelMap[appState.language] || "EN";
  }

  // 4. Synchronize Language Dropdown buttons active state
  document.querySelectorAll("#lang-dropdown-menu button[data-lang]").forEach(b => {
    b.classList.toggle("active", b.getAttribute("data-lang") === appState.language);
  });

  // 5. Synchronize Screen 2 Quick Sarvam buttons active state
  document.querySelectorAll(".sarvam-quick-lang-btn").forEach(b => {
    b.classList.toggle("active", b.getAttribute("data-quick-lang") === appState.language);
  });

  // 5b. Persist selected language across page refreshes
  try { localStorage.setItem("easyrail_lang", appState.language); } catch(e) {}

  // 5c. Update station input fields to show localized station names
  const fromInput = document.getElementById("from-station-input");
  const toInput   = document.getElementById("to-station-input");
  if (fromInput && appState.fromStation && appState.fromStation.code) {
    fromInput.value = getLocalizedStationName(appState.fromStation.code);
  }
  if (toInput && appState.toStation && appState.toStation.code) {
    toInput.value = getLocalizedStationName(appState.toStation.code);
  }

  // 5d. Update results summary bar (route + meta) with active language
  const routeSummaryEl = document.getElementById("results-summary-route");
  const metaSummaryEl  = document.getElementById("results-summary-meta");
  if (routeSummaryEl && appState.fromStation && appState.toStation) {
    routeSummaryEl.textContent = buildSummaryRoute(appState.fromStation.code, appState.toStation.code);
  }
  if (metaSummaryEl && appState.journeyDate) {
    metaSummaryEl.textContent = buildSummaryMeta(appState.journeyDate, appState.passengersCount, appState.quota);
  }

  // 5e. Re-render Screen 1 FAQ accordion content in active language
  if (typeof renderFAQAccordion === "function") {
    renderFAQAccordion();
  }

  // 6. Non-destructively re-render active screen dynamic components
  if (appState.currentScreen === 2) {
    renderTrains();
  } else if (appState.currentScreen === 3 && appState.selectedTrain) {
    renderClasses(appState.selectedTrain);
  } else if (appState.currentScreen === 4 && appState.selectedTrain) {
    updateJourneySummaryAccordion();
    renderPassengerForms();
  } else if (appState.currentScreen === 5) {
    renderFareBreakdown();
  } else if (appState.currentScreen === 6 && appState.bookingsHistory.length > 0) {
    renderTicket(appState.bookingsHistory[0]);
  }
}

function showToast(message, icon = "ℹ️") {
  const container = document.getElementById("toast-container");
  if (!container) return;
  
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerHTML = `<span>${icon}</span><span>${message}</span>`;
  container.appendChild(toast);
  
  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateY(10px)";
    toast.style.transition = "all 0.3s ease";
    setTimeout(() => toast.remove(), 300);
  }, 3200);
}


// --- Simplified Rail Madad 139 & Payment Safety Helper ---
function getSimplifiedRailMadadHtml(lang = "en") {
  if (lang === "hi") {
    return `
      <div style="display:flex;flex-direction:column;gap:12px;">
        <div style="padding:10px 12px;background:#f0fdf4;border-radius:8px;border:1px solid #bcf0cc;">
          🔒 <strong>सुरक्षित भुगतान एवं स्वतः रिफंड:</strong> लेन-देन विफल होने या चार्ट बनने के बाद अपुष्ट वेटलिस्ट टिकटों का 100% पूरा रिफंड कुछ ही मिनटों में सीधे मूल बैंक खाते में जमा हो जाता है।
        </div>

        <div style="padding:14px;background:#f6faf7;border-radius:10px;border:1.5px solid #d0e4d6;">
          <div style="font-weight:800;color:var(--color-primary);font-size:0.98rem;margin-bottom:6px;">
            📞 डायल 139 (रेल मदद)
          </div>
          <p style="font-size:0.86rem;color:var(--color-text);margin-bottom:10px;line-height:1.45;">
            भारतीय रेलवे में लगभग हर समस्या, पूछताछ या आपात स्थिति के लिए 139 डायल करें। यह साधारण फोन और स्मार्टफोन दोनों पर 12 भाषाओं में 24x7 उपलब्ध है।
          </p>

          <div style="font-weight:700;color:var(--color-primary);font-size:0.9rem;margin-bottom:6px;">
            139 पर IVRS मेनू विकल्प:
          </div>
          <div style="display:flex;flex-direction:column;gap:6px;font-size:0.84rem;line-height:1.45;">
            <div>• <strong>1 दबाएं:</strong> सुरक्षा और चिकित्सा सहायता (सीधे अधिकारी से बात)</div>
            <div>• <strong>2 दबाएं:</strong> सामान्य / ट्रेन पूछताछ (पीएनआर, आगमन/प्रस्थान, किराया, बुकिंग, भोजन, व्हीलचेयर)</div>
            <div>• <strong>4 दबाएं:</strong> सामान्य शिकायतें</div>
            <div>• <strong>5 दबाएं:</strong> सतर्कता (विजिलेंस) शिकायतें</div>
            <div>• <strong>6 दबाएं:</strong> पार्सल या माल ढुलाई</div>
            <div>• <strong>7 दबाएं:</strong> आईआरसीटीसी ट्रेनें</div>
            <div>• <strong>9 दबाएं:</strong> शिकायत की स्थिति</div>
            <div>• <strong>* (स्टार दबाएं):</strong> सीधे कॉल सेंटर एग्जीक्यूटिव से बात करें</div>
          </div>
        </div>

        <div style="padding:12px;background:#fafafa;border-radius:10px;border:1px solid #e2e8e4;font-size:0.84rem;">
          <div style="font-weight:700;color:var(--color-text);font-size:0.9rem;margin-bottom:6px;">
            अन्य उपयोगी नंबर और माध्यम:
          </div>
          <div style="display:flex;flex-direction:column;gap:6px;line-height:1.45;">
            <div>• <strong>1098:</strong> चाइल्डलाइन (खोए या संकटग्रस्त बच्चे)</div>
            <div>• <strong>139 (SMS):</strong> PNR, आगमन/प्रस्थान (AD), सीट उपलब्धता (SEAT), किराया (FARE), समय सारिणी (TIME) या स्पॉट (SPOT) के लिए एसएमएस भेजें।</div>
            <div>• <strong>रेल मदद ऐप / वेब:</strong> आधिकारिक रेल मदद ऐप या वेबसाइट पर ऑनलाइन शिकायत दर्ज और ट्रैक करें।</div>
          </div>
        </div>
      </div>
    `;
  }

  if (lang === "te") {
    return `
      <div style="display:flex;flex-direction:column;gap:12px;">
        <div style="padding:10px 12px;background:#f0fdf4;border-radius:8px;border:1px solid #bcf0cc;">
          🔒 <strong>సురక్షిత చెల్లింపులు & ఆటో-రీఫండ్:</strong> చెల్లింపు విఫలమైనా లేదా చార్ట్ తయారీ తర్వాత కన్ఫర్మ్ కాని వెయిట్‌లిస్ట్ టిక్కెట్లకు 100% రీఫండ్ తక్షణమే అసలు బ్యాంక్ ఖాతాలో జమ చేయబడుతుంది.
        </div>

        <div style="padding:14px;background:#f6faf7;border-radius:10px;border:1.5px solid #d0e4d6;">
          <div style="font-weight:800;color:var(--color-primary);font-size:0.98rem;margin-bottom:6px;">
            📞 డయల్ 139 (రైల్ మదద్)
          </div>
          <p style="font-size:0.86rem;color:var(--color-text);margin-bottom:10px;line-height:1.45;">
            భారతీయ రైల్వేలో దాదాపు ప్రతి సమస్య, విచారణ లేదా అత్యవసర పరిస్థితి కోసం 139 డయల్ చేయండి. ఇది సాధారణ మరియు స్మార్ట్‌ఫోన్లలో 12 భాషలలో 24x7 అందుబాటులో ఉంటుంది.
          </p>

          <div style="font-weight:700;color:var(--color-primary);font-size:0.9rem;margin-bottom:6px;">
            139 లో IVRS మెనూ ఎంపికలు:
          </div>
          <div style="display:flex;flex-direction:column;gap:6px;font-size:0.84rem;line-height:1.45;">
            <div>• <strong>1 నొక్కండి:</strong> భద్రత మరియు వైద్య సహాయం (ఎగ్జిక్యూటివ్‌తో కనెక్ట్ అవుతుంది)</div>
            <div>• <strong>2 నొక్కండి:</strong> సాధారణ / రైలు విచారణలు (PNR, రాక/బయలుదేరడం, ఛార్జీ, బుకింగ్, భోజనం, వీల్‌చైర్)</div>
            <div>• <strong>4 నొక్కండి:</strong> సాధారణ ఫిర్యాదులు</div>
            <div>• <strong>5 నొక్కండి:</strong> విజిలెన్స్ ఫిర్యాదులు</div>
            <div>• <strong>6 నొక్కండి:</strong> పార్సెల్ లేదా సరుకులు</div>
            <div>• <strong>7 నొక్కండి:</strong> IRCTC రైళ్లు</div>
            <div>• <strong>9 నొక్కండి:</strong> ఫిర్యాదు స్థితి</div>
            <div>• <strong>* (స్టార్ నొక్కండి):</strong> కాల్ సెంటర్ ఎగ్జిక్యూటివ్‌తో నేరుగా మాట్లాడండి</div>
          </div>
        </div>

        <div style="padding:12px;background:#fafafa;border-radius:10px;border:1px solid #e2e8e4;font-size:0.84rem;">
          <div style="font-weight:700;color:var(--color-text);font-size:0.9rem;margin-bottom:6px;">
            ఇతర సహాయక నంబర్లు & ఛానెల్‌లు:
          </div>
          <div style="display:flex;flex-direction:column;gap:6px;line-height:1.45;">
            <div>• <strong>1098:</strong> చైల్డ్‌లైన్ (తప్పిపోయిన లేదా రక్షణ అవసరమైన పిల్లల సహాయం)</div>
            <div>• <strong>139 (SMS):</strong> PNR, రాక/బయలుదేరడం (AD), సీటు లభ్యత (SEAT), ఛార్జీ (FARE), టైమ్‌టేబుల్ (TIME) లేదా స్పాట్ (SPOT) కోసం SMS పంపండి.</div>
            <div>• <strong>రైల్ మదద్ యాప్ / వెబ్:</strong> ఆన్‌లైన్‌లో ఫిర్యాదు నమోదు మరియు ట్రాకింగ్ చేయండి.</div>
          </div>
        </div>
      </div>
    `;
  }

  return `
    <div style="display:flex;flex-direction:column;gap:12px;">
      <div style="padding:10px 12px;background:#f0fdf4;border-radius:8px;border:1px solid #bcf0cc;">
        🔒 <strong>Safe Payments & Automatic Refunds:</strong> 100% simulated refund for unconfirmed waitlist tickets after chart preparation, credited directly back to your source account within minutes.
      </div>

      <div style="padding:14px;background:#f6faf7;border-radius:10px;border:1.5px solid #d0e4d6;">
        <div style="font-weight:800;color:var(--color-primary);font-size:0.98rem;margin-bottom:6px;">
          📞 Dial 139 (Rail Madad)
        </div>
        <p style="font-size:0.86rem;color:var(--color-text);margin-bottom:10px;line-height:1.45;">
          Dial 139 (Rail Madad) for almost every problem, query, or emergency in Indian Railways. It is available 24x7 in 12 languages on both basic phones and smartphones.
        </p>

        <div style="font-weight:700;color:var(--color-primary);font-size:0.9rem;margin-bottom:6px;">
          IVRS Menu Options on 139:
        </div>
        <div style="display:flex;flex-direction:column;gap:6px;font-size:0.84rem;line-height:1.45;">
          <div>• <strong>Press 1:</strong> Security and medical assistance (connects to an executive)</div>
          <div>• <strong>Press 2:</strong> General/train enquiries (PNR, arrival/departure, fare, booking, meals, wheelchair)</div>
          <div>• <strong>Press 4:</strong> General complaints</div>
          <div>• <strong>Press 5:</strong> Vigilance complaints</div>
          <div>• <strong>Press 6:</strong> Parcels or goods</div>
          <div>• <strong>Press 7:</strong> IRCTC trains</div>
          <div>• <strong>Press 9:</strong> Complaint status</div>
          <div>• <strong>Press * (star):</strong> Speak directly to a call center executive</div>
        </div>
      </div>

      <div style="padding:12px;background:#fafafa;border-radius:10px;border:1px solid #e2e8e4;font-size:0.84rem;">
        <div style="font-weight:700;color:var(--color-text);font-size:0.9rem;margin-bottom:6px;">
          Other Helpful Numbers & Channels:
        </div>
        <div style="display:flex;flex-direction:column;gap:6px;line-height:1.45;">
          <div>• <strong>1098:</strong> Childline (lost or missing children)</div>
          <div>• <strong>139 (SMS):</strong> Send SMS queries for PNR, train arrival/departure (AD), seat availability (SEAT), fare (FARE), timetable (TIME), or spot/locate (SPOT).</div>
          <div>• <strong>Rail Madad App / Web:</strong> Register or track complaints online via the official Press Information Bureau guidelines or the Rail Madad app.</div>
        </div>
      </div>
    </div>
  `;
}

// --- Screen 1 FAQ Accordion (Inline Slide-Down, No Popups) ---
function setupFAQAccordion() {
  document.querySelectorAll(".faq-trigger").forEach(btn => {
    btn.addEventListener("click", () => {
      const item = btn.closest(".faq-item");
      if (!item) return;
      const isOpen = item.classList.contains("open");
      
      document.querySelectorAll(".faq-item").forEach(other => {
        if (other !== item) {
          other.classList.remove("open");
          other.querySelector(".faq-trigger")?.setAttribute("aria-expanded", "false");
        }
      });
      
      if (!isOpen) {
        item.classList.add("open");
        btn.setAttribute("aria-expanded", "true");
        renderFAQAccordion();
      } else {
        item.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
      }
    });
  });
  renderFAQAccordion();
}

function renderFAQAccordion() {
  const lang = appState.language || "en";
  
  // 1. Classes
  const classesEl = document.getElementById("faq-content-classes");
  if (classesEl) {
    if (lang === "hi") {
      classesEl.innerHTML = `
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">SL (स्लीपर क्लास):</strong> खुली खिड़कियों और 3-टियर बर्थ (निचली, मध्य, ऊपरी + साइड लोअर, साइड अपर) वाला गैर-वातानुकूलित कोच। लंबी दूरी की किफायती यात्रा के लिए सर्वोत्तम।
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">3A (एसी 3 टियर):</strong> वातानुकूलित कोच जिसमें प्रति बे 3 बर्थ और 2 साइड बर्थ होती हैं। चादर, कंबल व तकिए दिए जाते हैं। आराम व बजट का सही संतुलन।
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">2A (एसी 2 टियर):</strong> अधिक चौड़े बर्थ, प्रति बे केवल 2 बर्थ (निचली व ऊपरी), व्यक्तिगत रीडिंग लैंप और गोपनीयता के लिए पर्दे।
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">1A (प्रथम श्रेणी एसी):</strong> लॉक होने वाले निजी केबिन (2 या 4 बर्थ)। पूर्ण प्रीमियम बिस्तर सामग्री और समर्पित अटेंडेंट सेवा।
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">CC (एसी चेयर कार):</strong> 3×2 लेआउट में रिक्लाइनिंग पुश-बैक सीटें। 6 घंटे से कम की दिन की यात्राओं के लिए सबसे सुविधाजनक।
          </div>
        </div>
      `;
    } else if (lang === "te") {
      classesEl.innerHTML = `
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">SL (స్లీపర్ క్లాస్):</strong> నాన్-ఏసీ కోచ్, విశాలమైన కిటికీలు మరియు 3-టైర్ బెర్తులు (దిగువ, మధ్య, పై + సైడ్ లోయర్, సైడ్ అప్పర్). బడ్జెట్ ప్రయాణానికి అత్యంత అనుకూలం.
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">3A (ఏసీ 3 టైర్):</strong> ఎయిర్ కండిషన్డ్ కోచ్, ప్రతి వైపు 3 బెర్తులు మరియు 2 సైడ్ బెర్తులు. దుప్పట్లు, బెడ్‌షీట్లు, దిండ్లు అందించబడతాయి.
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">2A (ఏసీ 2 టైర్):</strong> విస్తృత బెర్తులు, బే కి 2 బెర్తులు మాత్రమే, రీడింగ్ లైట్లు మరియు గోప్యతా కర్టెన్లు.
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">1A (ఫస్ట్ క్లాస్ ఏసీ):</strong> లాక్ చేయగల ప్రైవేట్ క్యాబిన్లు (2 లేదా 4 బెర్తులు), పూర్తి బెడ్డింగ్ మరియు అటెండెంట్ సేవ.
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">CC (ఏసీ చైర్ కార్):</strong> సౌకర్యవంతమైన పుష్-బ్యాక్ సీట్లు. 6 గంటల లోపు పగటి ప్రయాణాలకు ఉత్తమం.
          </div>
        </div>
      `;
    } else {
      classesEl.innerHTML = `
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">SL (Sleeper Class):</strong> Non-AC coach with open windows and 3-tier berths (Lower, Middle, Upper + Side Lower, Side Upper). Highly economical for long distance.
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">3A (AC 3 Tier):</strong> Air-conditioned coach with 3 berths on each side and 2 side berths. Blankets, bedsheets, and pillows provided. Great comfort and budget balance.
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">2A (AC 2 Tier):</strong> Wider berths, only 2 berths per bay (Lower & Upper), reading lights, and privacy curtains.
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">1A (AC First Class):</strong> Premium lockable private cabins (coupe with 2 berths or cabin with 4 berths). Includes full bedding and dedicated attendant.
          </div>
          <div style="padding:10px 12px;background:#f6faf7;border-radius:8px;border:1px solid #d8ebd9;">
            <strong style="color:var(--color-primary);">CC (AC Chair Car):</strong> Reclining push-back seats with 3×2 layout. Recommended for day journeys under 6 hours.
          </div>
        </div>
      `;
    }
  }

  // 2. Availability
  const availEl = document.getElementById("faq-content-availability");
  if (availEl) {
    if (lang === "hi") {
      availEl.innerHTML = `
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="padding:10px 12px;background:#f0fdf4;border-radius:8px;border:1px solid #bcf0cc;">
            <strong style="color:var(--color-success);">उपलब्ध (CNF):</strong> बर्थ तुरंत उपलब्ध हैं। भुगतान होते ही आपको कन्फर्म कोच और बर्थ संख्या आवंटित हो जाएगी।
          </div>
          <div style="padding:10px 12px;background:#fffbeb;border-radius:8px;border:1px solid #fbe39d;">
            <strong style="color:#b37905;">RAC (रद्दीकरण के विरुद्ध आरक्षण):</strong> आपको ट्रेन में यात्रा की 100% पक्की गारंटी मिलती है! दो RAC यात्री एक साइड लोअर बर्थ साझा करते हैं। अन्य यात्रियों के टिकट रद्द करने पर आपकी सीट पूरी बर्थ में स्वतः अपग्रेड हो जाती है।
          </div>
          <div style="padding:10px 12px;background:#fef2f2;border-radius:8px;border:1px solid #facfcf;">
            <strong style="color:var(--color-error);">वेटलिस्ट (WL):</strong> वर्तमान में कोई सीट उपलब्ध नहीं है। वेटलिस्ट ई-टिकट पर ट्रेन में यात्रा की अनुमति नहीं होती। यदि चार्ट बनने तक टिकट कन्फर्म नहीं होता, तो 100% रिफंड स्वतः बैंक खाते में आ जाता है।
          </div>
          <div style="padding:10px 12px;background:#f8faf8;border-radius:8px;border:1px solid #e1ebe3;">
            <strong>GNWL vs PQWL vs RLWL:</strong> GNWL (सामान्य वेटलिस्ट) की पुष्टि होने की संभावना सबसे अधिक होती है।
          </div>
        </div>
      `;
    } else if (lang === "te") {
      availEl.innerHTML = `
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="padding:10px 12px;background:#f0fdf4;border-radius:8px;border:1px solid #bcf0cc;">
            <strong style="color:var(--color-success);">లభ్యం (CNF):</strong> బెర్తులు అందుబాటులో ఉన్నాయి. చెల్లింపు పూర్తయిన వెంటనే కన్ఫర్మ్ కోచ్ మరియు బెర్త్ నంబర్ కేటాయించబడుతుంది.
          </div>
          <div style="padding:10px 12px;background:#fffbeb;border-radius:8px;border:1px solid #fbe39d;">
            <strong style="color:#b37905;">RAC (రద్దుకు వ్యతిరేకంగా రిజర్వేషన్):</strong> రైలులో ప్రయాణించడానికి హామీ లభిస్తుంది! ఇద్దరు ప్రయాణికులు ఒక సైడ్ లోయర్ బెర్త్‌ను పంచుకుంటారు. రద్దులు జరిగితే పూర్తి బెర్త్ లభిస్తుంది.
          </div>
          <div style="padding:10px 12px;background:#fef2f2;border-radius:8px;border:1px solid #facfcf;">
            <strong style="color:var(--color-error);">వెయిట్‌లిస్ట్ (WL):</strong> ప్రస్తుతం సీటు కేటాయించబడలేదు. వెయిట్‌లిస్ట్ ఈ-టికెట్‌పై ప్రయాణించడానికి అనుమతి లేదు. చార్ట్ తయారీ వరకు కన్ఫర్మ్ కాకపోతే 100% పూర్తి రీఫండ్ ఖాతాలో జమ అవుతుంది.
          </div>
          <div style="padding:10px 12px;background:#f8faf8;border-radius:8px;border:1px solid #e1ebe3;">
            <strong>GNWL వర్సెస్ PQWL:</strong> GNWL (సాధారణ వెయిట్‌లిస్ట్) కు కన్ఫర్మ్ అయ్యే అవకాశం అత్యధికంగా ఉంటుంది.
          </div>
        </div>
      `;
    } else {
      availEl.innerHTML = `
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="padding:10px 12px;background:#f0fdf4;border-radius:8px;border:1px solid #bcf0cc;">
            <strong style="color:var(--color-success);">AVAILABLE (CNF):</strong> Berths readily available. Confirmed coach and berth number assigned instantly upon payment.
          </div>
          <div style="padding:10px 12px;background:#fffbeb;border-radius:8px;border:1px solid #fbe39d;">
            <strong style="color:#b37905;">RAC (Reservation Against Cancellation):</strong> Guaranteed travel on the train! Two passengers share a side-lower berth. Upgraded to full berth when cancellations occur.
          </div>
          <div style="padding:10px 12px;background:#fef2f2;border-radius:8px;border:1px solid #facfcf;">
            <strong style="color:var(--color-error);">Waitlist (WL):</strong> No seat allotted currently. Travel not permitted on waitlisted e-ticket. If unconfirmed before chart preparation, 100% refund is credited automatically.
          </div>
          <div style="padding:10px 12px;background:#f8faf8;border-radius:8px;border:1px solid #e1ebe3;">
            <strong>GNWL vs PQWL vs RLWL:</strong> GNWL (General Waitlist) carries highest confirmation priority.
          </div>
        </div>
      `;
    }
  }

  // 3. Tatkal Rules
  const tatkalEl = document.getElementById("faq-content-tatkal");
  if (tatkalEl) {
    if (lang === "hi") {
      tatkalEl.innerHTML = `
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="padding:10px 12px;background:#fff8ea;border-radius:8px;border:1px solid #fce5b2;">
            ⏰ <strong>बुकिंग खुलने का समय:</strong> तत्काल बुकिंग प्रस्थान तिथि से <strong>ठीक 1 दिन पहले</strong> खुलती है:
            <ul style="margin:6px 0 0 18px;font-size:0.85rem;">
              <li><strong>सुबह 10:00 बजे:</strong> एसी श्रेणियां (1A, 2A, 3A, CC)</li>
              <li><strong>सुबह 11:00 बजे:</strong> गैर-एसी श्रेणियां (SL, 2S)</li>
            </ul>
          </div>
          <div style="padding:10px 12px;background:#f8faf9;border-radius:8px;border:1px solid #e1ece4;">
            💰 <strong>तत्काल अधिभार:</strong> सेकंड क्लास के लिए मूल किराये का 10% और अन्य श्रेणियों के लिए 30% (न्यूनतम ₹100, अधिकतम ₹500)।
          </div>
          <div style="padding:10px 12px;background:#fef2f2;border-radius:8px;border:1px solid #ffd8d8;">
            ⚠️ <strong>रद्दीकरण नियम:</strong> कन्फर्म तत्काल टिकट रद्द करने पर कोई रिफंड नहीं दिया जाता। वेटलिस्ट तत्काल टिकट स्वतः रिफंड हो जाते हैं।
          </div>
        </div>
      `;
    } else if (lang === "te") {
      tatkalEl.innerHTML = `
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="padding:10px 12px;background:#fff8ea;border-radius:8px;border:1px solid #fce5b2;">
            ⏰ <strong>బుకింగ్ ప్రారంభ సమయం:</strong> తత్కాల్ బుకింగ్ ప్రయాణ తేదీకి <strong>1 రోజు ముందు మాత్రమే</strong> ప్రారంభమవుతుంది:
            <ul style="margin:6px 0 0 18px;font-size:0.85rem;">
              <li><strong>ఉదయం 10:00 గం.:</strong> ఏసీ తరగతులు (1A, 2A, 3A, CC)</li>
              <li><strong>ఉదయం 11:00 గం.:</strong> నాన్-ఏసీ తరగతులు (SL, 2S)</li>
            </ul>
          </div>
          <div style="padding:10px 12px;background:#f8faf9;border-radius:8px;border:1px solid #e1ece4;">
            💰 <strong>తత్కాల్ రుసుము:</strong> సెకండ్ క్లాస్‌కు 10% మరియు ఇతర తరగతులకు 30% (కనీసం ₹100, గరిష్టం ₹500).
          </div>
          <div style="padding:10px 12px;background:#fef2f2;border-radius:8px;border:1px solid #ffd8d8;">
            ⚠️ <strong>రద్దు నియమాలు:</strong> కన్ఫర్మ్ తత్కాల్ టిక్కెట్లకు రీఫండ్ లభించదు. వెయిట్‌లిస్ట్ తత్కాల్ టిక్కెట్లు స్వయంచాలకంగా రీఫండ్ అవుతాయి.
          </div>
        </div>
      `;
    } else {
      tatkalEl.innerHTML = `
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="padding:10px 12px;background:#fff8ea;border-radius:8px;border:1px solid #fce5b2;">
            ⏰ <strong>Booking Opening Time:</strong> Tatkal booking opens strictly <strong>1 day prior</strong> to departure:
            <ul style="margin:6px 0 0 18px;font-size:0.85rem;">
              <li><strong>10:00 AM:</strong> AC Classes (1A, 2A, 3A, CC)</li>
              <li><strong>11:00 AM:</strong> Non-AC Classes (SL, 2S)</li>
            </ul>
          </div>
          <div style="padding:10px 12px;background:#f8faf9;border-radius:8px;border:1px solid #e1ece4;">
            💰 <strong>Tatkal Surcharges:</strong> 10% of base fare for second class, 30% for all AC & sleeper classes (min ₹100, max ₹500).
          </div>
          <div style="padding:10px 12px;background:#fef2f2;border-radius:8px;border:1px solid #ffd8d8;">
            ⚠️ <strong>Cancellation Policy:</strong> Zero refund on cancellation of confirmed Tatkal tickets. Waitlisted Tatkal tickets refunded automatically.
          </div>
        </div>
      `;
    }
  }

  // 4. Payment, Refunds & Rail Madad 139 Simplified
  const safetyEl = document.getElementById("faq-content-safety");
  if (safetyEl) {
    safetyEl.innerHTML = getSimplifiedRailMadadHtml(lang);
  }
}

// --- 7. Screen 1: Search, Stations & Autocomplete ---
function initSearch() {
  const dateInput = document.getElementById("journey-date-input");
  const today = new Date();
  const yyyy = today.getFullYear();
  const mm = String(today.getMonth() + 1).padStart(2, "0");
  const dd = String(today.getDate()).padStart(2, "0");
  const minDateStr = `${yyyy}-${mm}-${dd}`;
  
  if (dateInput) {
    dateInput.min = minDateStr;
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    const tmY = tomorrow.getFullYear();
    const tmM = String(tomorrow.getMonth() + 1).padStart(2, "0");
    const tmD = String(tomorrow.getDate()).padStart(2, "0");
    dateInput.value = `${tmY}-${tmM}-${tmD}`;
    appState.date = dateInput.value;
    appState.journeyDate = dateInput.value;
    
    dateInput.addEventListener("change", (e) => {
      appState.date = e.target.value;
      appState.journeyDate = e.target.value;
    });
  }
  
  // Date shortcut buttons
  document.getElementById("btn-date-today")?.addEventListener("click", () => {
    if (dateInput) {
      dateInput.value = minDateStr;
      appState.date = minDateStr;
      appState.journeyDate = minDateStr;
    }
  });
  
  document.getElementById("btn-date-tomorrow")?.addEventListener("click", () => {
    if (dateInput) {
      const d = new Date();
      d.setDate(d.getDate() + 1);
      const str = d.toISOString().split("T")[0];
      dateInput.value = str;
      appState.date = str;
      appState.journeyDate = str;
    }
  });
  
  document.getElementById("btn-date-dayafter")?.addEventListener("click", () => {
    if (dateInput) {
      const d = new Date();
      d.setDate(d.getDate() + 2);
      const str = d.toISOString().split("T")[0];
      dateInput.value = str;
      appState.date = str;
      appState.journeyDate = str;
    }
  });
  
  // Passenger Stepper
  const stepperMinus = document.getElementById("stepper-minus");
  const stepperPlus = document.getElementById("stepper-plus");
  const stepperCount = document.getElementById("stepper-count");
  
  stepperMinus?.addEventListener("click", () => {
    if (appState.passengersCount > 1) {
      appState.passengersCount--;
      appState.passengerCount = appState.passengersCount;
      appState.passengers = appState.passengersCount;
      if (stepperCount) stepperCount.textContent = appState.passengersCount;
    }
  });
  
  stepperPlus?.addEventListener("click", () => {
    if (appState.passengersCount < 6) {
      appState.passengersCount++;
      appState.passengerCount = appState.passengersCount;
      appState.passengers = appState.passengersCount;
      if (stepperCount) stepperCount.textContent = appState.passengersCount;
    } else {
      showToast("Maximum 6 passengers allowed per booking.", "⚠️");
    }
  });
  
  // Quota cards
  const quotaCards = document.querySelectorAll(".quota-card");
  quotaCards.forEach(card => {
    card.addEventListener("click", () => {
      quotaCards.forEach(c => c.classList.remove("active"));
      card.classList.add("active");
      const radio = card.querySelector("input[type='radio']");
      if (radio) {
        radio.checked = true;
        appState.quota = radio.value;
        appState.tatkalMode = (radio.value === "Tatkal");
        if (appState.tatkalMode && !isTomorrow(appState.journeyDate)) {
          const tmFmt = formatDate(getTomorrowDateStr());
          const msg = appState.language === "hi" 
            ? `तत्काल टिकट केवल कल (${tmFmt}) की यात्रा के लिए खुलते हैं`
            : appState.language === "te"
            ? `తత్కాల్ టిక్కెట్లు రేపటి (${tmFmt}) ప్రయాణానికి మాత్రమే తెరవబడతాయి`
            : `Tatkal tickets only open 1 day prior (${tmFmt})`;
          showToast(msg, "⚡");
        }
      }
    });
  });
  
  // Autocomplete setup
  setupStationAutocomplete("from-station-input", "from-autocomplete-list", (station) => {
    appState.fromStation = station;
    appState.from = station.code;
  });
  
  setupStationAutocomplete("to-station-input", "to-autocomplete-list", (station) => {
    appState.toStation = station;
    appState.to = station.code;
  });
  
  // Swap button
  document.getElementById("swap-stations-btn")?.addEventListener("click", swapStations);
  
  // Popular Station Chips
  document.querySelectorAll(".popular-chip").forEach(chip => {
    chip.addEventListener("click", () => {
      const code = chip.getAttribute("data-station") || chip.getAttribute("data-nearby");
      const station = stationsDB.find(s => s.code === code);
      if (!station) return;
      
      const parentInputGroup = chip.closest(".station-input-group");
      if (parentInputGroup) {
        const input = parentInputGroup.querySelector(".text-input");
        if (input && input.id.includes("from")) {
          appState.fromStation = station;
          appState.from = station.code;
          input.value = getLocalizedStationName(station.code);
        } else if (input && input.id.includes("to")) {
          appState.toStation = station;
          appState.to = station.code;
          input.value = getLocalizedStationName(station.code);
        }
      } else if (chip.hasAttribute("data-nearby")) {
        appState.toStation = station;
        appState.to = station.code;
        const toInput = document.getElementById("to-station-input");
        if (toInput) toInput.value = getLocalizedStationName(station.code);
        appState.noResultsDemo = false;
        renderTrains();
      }
    });
  });
  
  // Submit Search CTA
  document.getElementById("search-trains-submit-btn")?.addEventListener("click", handleSearch);
  
  // Setup Screen 1 Inline Slide-Down FAQ Accordion
  setupFAQAccordion();
}

function swapStations() {
  const fromInput = document.getElementById("from-station-input");
  const toInput = document.getElementById("to-station-input");
  
  const tempStation = appState.fromStation;
  appState.fromStation = appState.toStation;
  appState.toStation = tempStation;
  
  appState.from = appState.fromStation.code;
  appState.to = appState.toStation.code;
  
  if (fromInput) fromInput.value = getLocalizedStationName(appState.fromStation.code);
  if (toInput) toInput.value = getLocalizedStationName(appState.toStation.code);
  
  showToast(`Swapped stations: ${appState.fromStation.code} ↔ ${appState.toStation.code}`, "🔄");
}

function setupStationAutocomplete(inputId, dropdownId, onSelect) {
  const input = document.getElementById(inputId);
  const dropdown = document.getElementById(dropdownId);
  if (!input || !dropdown) return;
  
  let currentFocus = -1;
  
  function renderList(matches) {
    dropdown.innerHTML = "";
    if (matches.length === 0) {
      dropdown.innerHTML = `<div style="padding: 12px; font-size: 0.85rem; color: var(--color-muted);">No matching stations found.</div>`;
      dropdown.classList.add("open");
      return;
    }
    
    matches.forEach((stn, idx) => {
      const item = document.createElement("div");
      item.className = "autocomplete-item";
      item.setAttribute("role", "option");
      item.setAttribute("data-index", idx);
      item.innerHTML = `
        <div class="station-details">
          <span class="station-city">${stn.city}</span>
          <span class="station-name">${stn.name}, ${stn.state}</span>
        </div>
        <span class="station-code-badge">${stn.code}</span>
      `;
      
      item.addEventListener("click", () => {
        selectStation(stn);
      });
      
      dropdown.appendChild(item);
    });
    
    dropdown.classList.add("open");
  }
  
  function selectStation(stn) {
    input.value = getLocalizedStationName(stn.code) || `${stn.city} (${stn.code})`;
    dropdown.classList.remove("open");
    currentFocus = -1;
    onSelect(stn);
  }
  
  input.addEventListener("input", () => {
    const val = input.value.trim().toLowerCase();
    currentFocus = -1;
    if (!val) {
      renderList(stationsDB.slice(0, 8));
      return;
    }
    
    const matches = stationsDB.filter(s => 
      s.code.toLowerCase().includes(val) ||
      s.city.toLowerCase().includes(val) ||
      s.name.toLowerCase().includes(val)
    );
    renderList(matches);
  });
  
  input.addEventListener("focus", () => {
    const val = input.value.trim().toLowerCase();
    if (!val) {
      renderList(stationsDB.slice(0, 8));
    } else {
      const matches = stationsDB.filter(s => 
        s.code.toLowerCase().includes(val) ||
        s.city.toLowerCase().includes(val) ||
        s.name.toLowerCase().includes(val)
      );
      renderList(matches);
    }
  });
  
  input.addEventListener("keydown", (e) => {
    const items = dropdown.querySelectorAll(".autocomplete-item");
    if (!dropdown.classList.contains("open") || items.length === 0) return;
    
    if (e.key === "ArrowDown") {
      e.preventDefault();
      currentFocus++;
      if (currentFocus >= items.length) currentFocus = 0;
      setActiveItem(items);
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      currentFocus--;
      if (currentFocus < 0) currentFocus = items.length - 1;
      setActiveItem(items);
    } else if (e.key === "Enter") {
      e.preventDefault();
      if (currentFocus > -1 && items[currentFocus]) {
        items[currentFocus].click();
      }
    } else if (e.key === "Escape") {
      dropdown.classList.remove("open");
    }
  });
  
  function setActiveItem(items) {
    items.forEach(el => el.classList.remove("active"));
    if (currentFocus > -1 && items[currentFocus]) {
      items[currentFocus].classList.add("active");
      items[currentFocus].scrollIntoView({ block: "nearest" });
    }
  }
  
  document.addEventListener("click", (e) => {
    if (!input.contains(e.target) && !dropdown.contains(e.target)) {
      dropdown.classList.remove("open");
    }
  });
}

function handleSearch() {
  if (appState.fromStation.code === appState.toStation.code) {
    showToast("Source and destination stations cannot be the same.", "⚠️");
    return;
  }
  
  if (!appState.journeyDate) {
    showToast("Please choose a valid journey date.", "⚠️");
    return;
  }
  
  appState.from = appState.fromStation.code;
  appState.to = appState.toStation.code;
  appState.date = appState.journeyDate;
  
  const routeEl = document.getElementById("results-summary-route");
  const metaEl = document.getElementById("results-summary-meta");
  
  if (routeEl) {
    routeEl.textContent = buildSummaryRoute(appState.fromStation.code, appState.toStation.code);
  }
  if (metaEl) {
    metaEl.textContent = buildSummaryMeta(appState.journeyDate, appState.passengersCount, appState.quota);
  }
  
  renderTrains();
  showScreen(2);
}

// --- 8. Screen 2: Train Results & Filters ---
function renderTrains(trainList = trains) {
  const container = document.getElementById("trains-list-container");
  const noTrainsCard = document.getElementById("no-trains-found-card");
  if (!container || !noTrainsCard) return;
  
  container.innerHTML = "";

  // Tatkal 1-Day Prior Rule Check
  const existingBlockedCard = document.getElementById("tatkal-blocked-card");
  if (appState.quota === "Tatkal" || appState.tatkalMode) {
    if (!isTomorrow(appState.journeyDate)) {
      container.style.display = "none";
      noTrainsCard.style.display = "none";
      
      const tomorrowStr = getTomorrowDateStr();
      const tomorrowFormatted = formatDate(tomorrowStr);
      const selectedFormatted = formatDate(appState.journeyDate);
      
      let blockedCard = existingBlockedCard;
      if (!blockedCard) {
        blockedCard = document.createElement("div");
        blockedCard.id = "tatkal-blocked-card";
        blockedCard.className = "tatkal-date-blocked-card";
        container.parentNode.insertBefore(blockedCard, container);
      }
      blockedCard.style.display = "block";
      
      let titleText = "Tatkal Booking Opens 1 Day Prior Only";
      let descText = `Under Indian Railways rules, Tatkal quota bookings open strictly 1 day before departure (10:00 AM for AC, 11:00 AM for Non-AC). Tatkal booking is not yet open for your selected date (${selectedFormatted}). Tatkal is currently open only for tomorrow (${tomorrowFormatted}).`;
      let btnTomorrowText = `📅 Book Tatkal for Tomorrow (${tomorrowFormatted})`;
      let btnGeneralText = `👥 Switch to General Quota for ${selectedFormatted}`;
      
      if (appState.language === "hi") {
        titleText = "तत्काल बुकिंग केवल 1 दिन पहले खुलती है";
        descText = `भारतीय रेलवे नियमानुसार तत्काल बुकिंग यात्रा की तारीख से ठीक 1 दिन पहले खुलती है (एसी: सुबह 10:00 बजे, गैर-एसी: सुबह 11:00 बजे)। आपकी चुनी हुई तिथि (${selectedFormatted}) के लिए तत्काल टिकट अभी नहीं खुले हैं। वर्तमान में तत्काल केवल कल (${tomorrowFormatted}) के लिए उपलब्ध है।`;
        btnTomorrowText = `📅 कल (${tomorrowFormatted}) के लिए तत्काल ट्रेनें देखें`;
        btnGeneralText = `👥 ${selectedFormatted} के लिए सामान्य कोटा में देखें`;
      } else if (appState.language === "te") {
        titleText = "తత్కాల్ బుకింగ్ 1 రోజు ముందు మాత్రమే తెరుచుకుంటుంది";
        descText = `భారతీయ రైల్వే నిబంధనల ప్రకారం, తత్కాల్ బుకింగ్ ప్రయాణ తేదీకి ఖచ్చితంగా 1 రోజు ముందు మాత్రమే తెరుచుకుంటుంది (ఏసీ: ఉదయం 10:00 గం., నాన్-ఏసీ: ఉదయం 11:00 గం.). మీరు ఎంచుకున్న తేదీకి (${selectedFormatted}) తత్కాల్ టిక్కెట్లు ఇంకా తెరవబడలేదు. తత్కాల్ ప్రస్తుతం రేపటి (${tomorrowFormatted}) ప్రయాణానికి మాత్రమే అందుబాటులో ఉంది.`;
        btnTomorrowText = `📅 రేపటి (${tomorrowFormatted}) కోసం తత్కాల్ రైళ్లు చూడండి`;
        btnGeneralText = `👥 ${selectedFormatted} కోసం సాధారణ కోటాకు మారండి`;
      }
      
      blockedCard.innerHTML = `
        <div style="font-size: 2.2rem; margin-bottom: 8px;">⏳</div>
        <h3>${titleText}</h3>
        <p>${descText}</p>
        <div class="tatkal-blocked-actions">
          <button type="button" class="btn btn-primary" id="btn-tatkal-set-tomorrow">${btnTomorrowText}</button>
          <button type="button" class="btn btn-outline" id="btn-tatkal-set-general">${btnGeneralText}</button>
        </div>
      `;
      
      blockedCard.querySelector("#btn-tatkal-set-tomorrow")?.addEventListener("click", () => {
        appState.journeyDate = tomorrowStr;
        appState.date = tomorrowStr;
        const dateInput = document.getElementById("journey-date-input");
        if (dateInput) dateInput.value = tomorrowStr;
        applyTranslations();
        renderTrains();
        showToast("Switched to Tomorrow for Tatkal booking", "⚡");
      });
      
      blockedCard.querySelector("#btn-tatkal-set-general")?.addEventListener("click", () => {
        appState.quota = "General";
        appState.tatkalMode = false;
        const genRadio = document.querySelector('input[name="quota"][value="General"]');
        if (genRadio) {
          genRadio.checked = true;
          document.querySelectorAll(".quota-card").forEach(c => c.classList.remove("active"));
          genRadio.closest(".quota-card")?.classList.add("active");
        }
        applyTranslations();
        renderTrains();
        showToast("Switched to General Quota", "👥");
      });
      
      return;
    }
  }
  
  if (existingBlockedCard) {
    existingBlockedCard.style.display = "none";
  }
  
  if (appState.noResultsDemo) {
    container.style.display = "none";
    noTrainsCard.style.display = "block";
    renderAlternateDates();
    return;
  }
  
  const filtered = applyFilters(trainList);
  
  if (filtered.length === 0) {
    container.style.display = "none";
    noTrainsCard.style.display = "block";
    renderAlternateDates();
    return;
  }
  
  container.style.display = "flex";
  noTrainsCard.style.display = "none";
  
  filtered.forEach(train => {
    const card = document.createElement("div");
    card.className = "train-card";
    
    let typeClass = "";
    if (train.type === "Superfast") typeClass = "superfast";
    if (train.type === "Tatkal") typeClass = "tatkal";
    
    const allDays = ["M", "T", "W", "T", "F", "S", "S"];
    const localDays = getLocalizedDayLabels();
    const daysHtml = allDays.map((d, i) => {
      const isActive = train.runningDaysArray.includes(d) || train.days === "Daily";
      return `<span class="day-badge ${isActive ? 'active' : ''}">${localDays[i]}</span>`;
    }).join("");
    
    const classesHtml = train.classes.map(cls => {
      let statusBadge = "";
      if (cls.status === "AVAILABLE") {
        statusBadge = `<span class="status-pill status-available">${translate('statusAvailable')} ${cls.avail}</span>`;
      } else if (cls.status === "RAC") {
        statusBadge = `<span class="status-pill status-rac">${translate('statusRAC')} ${cls.avail}</span>`;
      } else {
        statusBadge = `<span class="status-pill status-wl">${translate('statusWL')} ${cls.wl || 34}</span>`;
      }
      
      return `
        <div class="class-mini-card" data-train-id="${train.id}" data-class-code="${cls.code}">
          <div class="class-mini-top">
            <span class="class-mini-code">${cls.code}</span>
            <span class="class-mini-fare">${formatCurrency(cls.fare)}</span>
          </div>
          <div class="class-mini-status">
            ${statusBadge}
          </div>
        </div>
      `;
    }).join("");
    
    const isOvernight = train.arr.includes("+1");
    
    card.innerHTML = `
      <div class="train-header-row">
        <div class="train-title-group">
          <div class="train-name-wrap">
            <span class="train-name">${getLocalizedTrainName(train.name)}</span>
          </div>
          <div class="train-tags-col">
            <span class="train-number">#${train.number}</span>
            <span class="train-type-badge ${typeClass}">${translateTrainType(train.type)}</span>
          </div>
        </div>
        <div class="running-days" title="${train.days === 'Daily' ? translate('runsDaily') : translate('runsOnDays')}">
          ${daysHtml}
        </div>
      </div>

      <div class="train-schedule-grid">
        <div class="schedule-point">
          <div class="point-time">${train.dep}</div>
          <div class="point-station">${getLocalizedStationName(appState.fromStation.code)}</div>
        </div>

        <div class="route-indicator">
          <span class="duration-text">${formatDuration(train.duration)}</span>
          <div class="route-line-visual">
            <span class="route-train-icon">🚆</span>
          </div>
        </div>

        <div class="schedule-point dest">
          <div class="point-time">${train.arr.replace('+1', '')} ${isOvernight ? `<span class="overnight-tag">${translate('overnightTag')}</span>` : ''}</div>
          <div class="point-station">${getLocalizedStationName(appState.toStation.code)}</div>
        </div>
      </div>

      <div class="train-classes-row">
        ${classesHtml}
      </div>

      <div class="train-card-footer">
        <div class="train-features">
          <span>${translate('catering')}</span>
          <span>${translate('charging')}</span>
          <span>${translate('security')}</span>
        </div>
        <button type="button" class="btn btn-primary btn-select-train" data-train-id="${train.id}">
          ${translate('bookNow')}
        </button>
      </div>
    `;
    
    card.querySelectorAll(".class-mini-card").forEach(miniCard => {
      miniCard.addEventListener("click", () => {
        const trainId = parseInt(miniCard.getAttribute("data-train-id"));
        const classCode = miniCard.getAttribute("data-class-code");
        proceedToClassSelection(trainId, classCode);
      });
    });
    
    card.querySelector(".btn-select-train")?.addEventListener("click", () => {
      proceedToClassSelection(train.id, train.classes[0].code);
    });
    
    container.appendChild(card);
  });
}

function applyFilters(list = trains) {
  return list.filter(t => {
    if (appState.currentFilter === "all") return true;
    if (appState.currentFilter === "morning") {
      const depHour = parseInt(t.dep.split(":")[0]);
      return depHour >= 6 && depHour < 12;
    }
    if (appState.currentFilter === "evening") {
      const depHour = parseInt(t.dep.split(":")[0]);
      return depHour >= 18 && depHour <= 23;
    }
    if (appState.currentFilter === "ac") {
      return t.classes.some(c => ["3A", "2A", "1A", "CC"].includes(c.code));
    }
    if (appState.currentFilter === "non-ac") {
      return t.classes.some(c => c.code === "SL");
    }
    if (appState.currentFilter === "available") {
      return t.classes.some(c => c.status === "AVAILABLE");
    }
    if (appState.currentFilter === "superfast") {
      return t.type === "Superfast";
    }
    return true;
  });
}

function renderAlternateDates() {
  const container = document.getElementById("alternate-dates-chips");
  if (!container) return;
  container.innerHTML = "";
  
  const baseDate = appState.journeyDate ? new Date(appState.journeyDate + "T00:00:00") : new Date();
  
  [1, 2, 3].forEach(offset => {
    const d = new Date(baseDate);
    d.setDate(d.getDate() + offset);
    const dateStr = d.toISOString().split("T")[0];
    const label = d.toLocaleDateString("en-IN", { day: "numeric", month: "short", weekday: "short" });
    
    const chip = document.createElement("button");
    chip.type = "button";
    chip.className = "alternate-date-chip";
    chip.textContent = `${label} (+${offset}d)`;
    chip.addEventListener("click", () => {
      appState.journeyDate = dateStr;
      appState.date = dateStr;
      const dateInput = document.getElementById("journey-date-input");
      if (dateInput) dateInput.value = dateStr;
      
      const metaEl = document.getElementById("results-summary-meta");
      if (metaEl) {
        metaEl.textContent = buildSummaryMeta(appState.journeyDate, appState.passengersCount, appState.quota);
      }
      
      appState.noResultsDemo = false;
      renderTrains();
      showToast(`Updated journey date to ${label}`, "📅");
    });
    container.appendChild(chip);
  });
}

function setupScreen2Listeners() {
  document.getElementById("btn-back-to-search")?.addEventListener("click", () => {
    showScreen(1);
  });
  
  document.getElementById("btn-modify-search")?.addEventListener("click", () => {
    showScreen(1);
  });
  
  document.querySelectorAll(".filter-chip").forEach(chip => {
    chip.addEventListener("click", () => {
      document.querySelectorAll(".filter-chip").forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      appState.currentFilter = chip.getAttribute("data-filter");
      appState.noResultsDemo = false;
      renderTrains();
    });
  });
  
  document.getElementById("btn-toggle-no-results-demo")?.addEventListener("click", () => {
    appState.noResultsDemo = !appState.noResultsDemo;
    renderTrains();
    if (appState.noResultsDemo) {
      showToast("Showing demo empty state: No trains found.", "ℹ️");
    } else {
      showToast("Restored train search results.", "✓");
    }
  });
  
  document.getElementById("btn-reset-filters")?.addEventListener("click", () => {
    appState.noResultsDemo = false;
    appState.currentFilter = "all";
    document.querySelectorAll(".filter-chip").forEach(c => c.classList.remove("active"));
    const allChip = document.querySelector(".filter-chip[data-filter='all']");
    if (allChip) allChip.classList.add("active");
    renderTrains();
  });

  // Sarvam AI Quick Language Switch Buttons
  document.querySelectorAll(".sarvam-quick-lang-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const selectedLang = btn.getAttribute("data-quick-lang");
      appState.language = selectedLang;
      applyTranslations();
      const names = { en: "English", hi: "हिन्दी", te: "తెలుగు" };
      showToast(`View translated to ${names[selectedLang]} with Sarvam AI ✨`, "🌐");
    });
  });

  document.getElementById("btn-results-open-sarvam")?.addEventListener("click", () => {
    openSarvamStudioModal();
  });
}

// --- 9. Screen 3: Class & Seat Selection ---
function proceedToClassSelection(trainId, preselectedClassCode = null) {
  const train = trains.find(t => t.id === trainId);
  if (!train) return;
  appState.selectedTrain = train;
  
  const titleEl = document.getElementById("class-screen-train-name");
  const metaEl = document.getElementById("class-screen-train-meta");
  const quotaBadge = document.getElementById("class-screen-quota-badge");
  
  if (titleEl) titleEl.textContent = `${train.name} (${train.number})`;
  if (metaEl) metaEl.textContent = `${train.dep} ${appState.fromStation.code} → ${train.arr} ${appState.toStation.code} (${train.duration}) · ${train.days}`;
  if (quotaBadge) quotaBadge.textContent = getLocalizedQuota(appState.quota);
  
  renderClasses(train, preselectedClassCode);
  updateTatkalTimer();
  
  showScreen(3);
}

function renderClasses(train = appState.selectedTrain, preselectedCode = null) {
  const container = document.getElementById("classes-detail-grid");
  if (!container || !train) return;
  container.innerHTML = "";
  
  train.classes.forEach(cls => {
    const card = document.createElement("div");
    card.className = "class-card";
    
    const info = getLocalizedClassInfo(cls.code, cls.name);
    
    let statusPill = "";
    let alertBox = "";
    
    if (cls.status === "AVAILABLE") {
      statusPill = `<span class="status-pill status-available">${translate('statusAvailable')} (${cls.avail})</span>`;
      alertBox = `<div class="class-note-alert avl">✅ <strong>${translate('immediateConfirm')}</strong></div>`;
    } else if (cls.status === "RAC") {
      statusPill = `<span class="status-pill status-rac">${translate('statusRAC')}-${cls.avail}</span>`;
      alertBox = `<div class="class-note-alert rac">ℹ️ <strong>${translate('racNote')}</strong></div>`;
    } else {
      statusPill = `<span class="status-pill status-wl">${translate('statusWL')}-${cls.wl || 34}</span>`;
      alertBox = `<div class="class-note-alert wl">⚠️ <strong>${translate('wlNote')}</strong></div>`;
    }
    
    let effectiveFare = cls.fare;
    if (appState.quota === "Tatkal" || appState.tatkalMode) {
      const surcharge = (cls.code === "SL" ? 150 : 350);
      effectiveFare += surcharge;
    }
    
    card.innerHTML = `
      <div class="class-card-top">
        <div class="class-card-name">
          <h4>${info.fullName}</h4>
          <span style="font-size: 0.8rem; color: var(--color-muted);">${info.badge}</span>
        </div>
        <span class="class-code-tag">${cls.code}</span>
      </div>

      <div class="berth-visual-box">
        <span style="font-size: 1.8rem;">${info.icon}</span>
        <div style="font-size: 0.82rem; color: var(--color-text);">
          <div><strong>Berth Configuration:</strong></div>
          <span style="color: var(--color-muted);">${cls.code === 'CC' ? '2x3 Reclining Seats' : cls.code === '1A' ? '2/4 Berths Private Coupe' : cls.code === '2A' ? '2 Berths Per Bay (Lower/Upper)' : '3 Berths Per Bay (Lower/Middle/Upper)'}</span>
        </div>
      </div>

      <p class="class-description">${info.desc}</p>

      <div class="class-fare-box">
        <span class="class-fare-label">${translate('baseFare')}:</span>
        <span class="class-fare-amount">${formatCurrency(effectiveFare)}</span>
      </div>

      <div class="class-availability-row">
        <span style="font-size: 0.82rem; font-weight: 700; color: var(--color-muted);">Status:</span>
        ${statusPill}
      </div>

      ${alertBox}

      <button type="button" class="btn btn-primary btn-block btn-select-this-class" data-class-code="${cls.code}">
        ${translate('selectThisClass')}
      </button>
    `;
    
    card.querySelector(".btn-select-this-class")?.addEventListener("click", () => {
      appState.selectedClass = { ...cls, effectiveFare };
      if (cls.status === "WL") {
        handleWLSelection(cls);
      } else {
        proceedToPassengerDetails();
      }
    });
    
    container.appendChild(card);
  });
}

function handleWLSelection(cls = appState.selectedClass) {
  appState.pendingWLClass = cls;
  const modal = document.getElementById("modal-wl-advisory");
  const heading = document.getElementById("wl-modal-status-heading");
  if (heading) heading.textContent = `This train is on Waitlist (WL-${cls.wl || 34})`;
  if (modal) modal.classList.add("open");
}

function updateTatkalTimer() {
  const banner = document.getElementById("tatkal-notice-banner");
  if (!banner) return;
  
  if (appState.quota === "Tatkal" || appState.tatkalMode) {
    banner.style.display = "flex";
  } else {
    banner.style.display = "none";
    return;
  }
  
  const badge = document.getElementById("tatkal-countdown-badge");
  const title = document.getElementById("tatkal-banner-title");
  const desc = document.getElementById("tatkal-banner-desc");
  if (!badge) return;
  
  if (appState.simulateTatkalClock === "before10") {
    if (title) title.textContent = "⚡ Tatkal AC Window Opens at 10:00 AM";
    if (desc) desc.textContent = "Simulated Time: 08:45 AM. Tatkal AC booking opens at 10:00 AM. Opens in 1 hour 15 minutes. Non-AC at 11:00 AM. (+Tatkal surcharge applicable)";
    badge.textContent = "Opens in: 01h 15m";
    badge.style.background = "#8c5500";
  } else if (appState.simulateTatkalClock === "between1011") {
    if (title) title.textContent = "🟢 AC Tatkal is NOW OPEN!";
    if (desc) desc.textContent = "Simulated Time: 10:20 AM. AC Tatkal open, Non-AC not yet (opens at 11:00 AM in 40 minutes).";
    badge.textContent = "AC OPEN · SL in 40m";
    badge.style.background = "var(--color-primary)";
  } else {
    if (title) title.textContent = "🟢 Tatkal Booking is Active for ALL Classes";
    if (desc) desc.textContent = "Simulated Time: 11:15 AM. Tatkal booking is open for both AC and Non-AC classes (normal booking flow).";
    badge.textContent = "Tatkal Active";
    badge.style.background = "var(--color-primary)";
  }
}

function setupScreen3Listeners() {
  document.getElementById("btn-back-to-results")?.addEventListener("click", () => {
    showScreen(2);
  });
  
  document.querySelectorAll(".tatkal-demo-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const mode = btn.getAttribute("data-time-sim");
      appState.simulateTatkalClock = mode;
      updateTatkalTimer();
      showToast(`Simulated Tatkal Clock: ${btn.textContent}`, "⏰");
    });
  });
  
  document.getElementById("btn-wl-choose-another")?.addEventListener("click", () => {
    document.getElementById("modal-wl-advisory")?.classList.remove("open");
    showScreen(2);
  });
  
  document.getElementById("btn-wl-continue")?.addEventListener("click", () => {
    document.getElementById("modal-wl-advisory")?.classList.remove("open");
    proceedToPassengerDetails();
  });
}

// --- 10. Screen 4: Passenger Forms & Validation ---
function proceedToPassengerDetails() {
  updateJourneySummaryAccordion();
  renderPassengerForms();
  showScreen(4);
}

function updateJourneySummaryAccordion() {
  const train = appState.selectedTrain;
  const cls = appState.selectedClass;
  if (!train || !cls) return;
  
  const titleEl = document.getElementById("accordion-title-summary");
  const trainEl = document.getElementById("summary-train-val");
  const routeEl = document.getElementById("summary-route-val");
  const classEl = document.getElementById("summary-class-val");
  const fareEl = document.getElementById("summary-fare-val");
  
  if (titleEl) titleEl.textContent = `Journey Summary: ${train.name} (${train.number}) · ${cls.code}`;
  if (trainEl) trainEl.textContent = `${train.number} ${train.name}`;
  if (routeEl) routeEl.textContent = `${appState.fromStation.code} → ${appState.toStation.code} (${formatDate(appState.journeyDate)})`;
  if (classEl) classEl.textContent = `${getLocalizedClassInfo(cls.code).fullName} (${cls.code}) · ${getLocalizedQuota(appState.quota)}`;
  if (fareEl) fareEl.textContent = `${formatCurrency(cls.effectiveFare)}`;
}

function renderPassengerForms() {
  const container = document.getElementById("passenger-forms-container");
  if (!container) return;
  container.innerHTML = "";
  
  const count = appState.passengersCount;
  if (appState.passengersList.length !== count) {
    appState.passengersList = [];
    for (let i = 0; i < count; i++) {
      appState.passengersList.push({
        id: i + 1,
        name: i === 0 ? "Rahul Sharma" : "",
        age: i === 0 ? 32 : "",
        gender: "Male",
        berthPreference: "No Preference",
        isSenior: false
      });
    }
  }
  
  appState.passengersList.forEach((p) => {
    const card = document.createElement("div");
    card.className = "passenger-card";
    card.setAttribute("data-passenger-id", p.id);
    
    card.innerHTML = `
      <div class="passenger-card-header">
        <div class="passenger-badge-title">
          <span class="passenger-num-pill">${p.id}</span>
          <span>${translate('passenger')} ${p.id}</span>
        </div>
        <span style="font-size: 0.8rem; color: var(--color-muted);">${translate('adultNotice')}</span>
      </div>

      <div class="passenger-grid">
        <div class="form-group">
          <label for="p-name-${p.id}">${translate('fullNameLabel')}</label>
          <div class="form-input-wrap">
            <input type="text" id="p-name-${p.id}" class="form-control p-name-input ${p.name ? 'is-valid' : ''}" placeholder="${translate('fullNamePlaceholder')}" value="${p.name}" required>
            <span class="input-valid-icon">✓</span>
          </div>
          <div class="error-text">${translate('valNameError')}</div>
        </div>

        <div class="form-group">
          <label for="p-age-${p.id}">${translate('ageLabel')}</label>
          <div class="form-input-wrap">
            <input type="number" id="p-age-${p.id}" class="form-control p-age-input ${p.age ? 'is-valid' : ''}" placeholder="${translate('ageLabel')}" min="1" max="99" value="${p.age}" required>
            <span class="input-valid-icon">✓</span>
          </div>
          <div class="error-text">${translate('valAgeError')}</div>
        </div>

        <div class="form-group">
          <label>${translate('genderLabel')}</label>
          <div class="gender-pills-group" role="radiogroup">
            <label class="gender-pill ${p.gender === 'Male' ? 'active' : ''}">
              <input type="radio" name="p-gender-${p.id}" value="Male" ${p.gender === 'Male' ? 'checked' : ''}>
              ${translate('genderMale')}
            </label>
            <label class="gender-pill ${p.gender === 'Female' ? 'active' : ''}">
              <input type="radio" name="p-gender-${p.id}" value="Female" ${p.gender === 'Female' ? 'checked' : ''}>
              ${translate('genderFemale')}
            </label>
            <label class="gender-pill ${p.gender === 'Other' ? 'active' : ''}">
              <input type="radio" name="p-gender-${p.id}" value="Other" ${p.gender === 'Other' ? 'checked' : ''}>
              ${translate('genderOther')}
            </label>
          </div>
        </div>

        <div class="form-group">
          <label for="p-berth-${p.id}">${translate('berthPrefLabel')} <span style="font-weight:400; font-size:0.75rem;">${translate('berthSubject')}</span></label>
          <select id="p-berth-${p.id}" class="form-control p-berth-select">
            <option value="No Preference" ${p.berthPreference === 'No Preference' ? 'selected' : ''}>${translate('noPref')}</option>
            <option value="Lower" ${p.berthPreference === 'Lower' ? 'selected' : ''}>${translate('lowerBerth')}</option>
            <option value="Middle" ${p.berthPreference === 'Middle' ? 'selected' : ''}>${translate('middleBerth')}</option>
            <option value="Upper" ${p.berthPreference === 'Upper' ? 'selected' : ''}>${translate('upperBerth')}</option>
            <option value="Side Lower" ${p.berthPreference === 'Side Lower' ? 'selected' : ''}>${translate('sideLowerBerth')}</option>
            <option value="Side Upper" ${p.berthPreference === 'Side Upper' ? 'selected' : ''}>${translate('sideUpperBerth')}</option>
          </select>
        </div>
      </div>

      <label class="senior-check-row">
        <input type="checkbox" class="p-senior-check" id="p-senior-${p.id}" ${p.isSenior ? 'checked' : ''}>
        <span class="senior-check-label">Senior Citizen (Priority lower berth for passengers aged 60+)</span>
        <span class="senior-discount-badge" id="senior-badge-${p.id}" style="${p.isSenior ? 'display: inline-block;' : 'display: none;'}">Lower Berth Priority</span>
      </label>
    `;
    
    const nameInput = card.querySelector(".p-name-input");
    const ageInput = card.querySelector(".p-age-input");
    const seniorCheck = card.querySelector(".p-senior-check");
    const seniorBadge = card.querySelector(`#senior-badge-${p.id}`);
    const genderPills = card.querySelectorAll(".gender-pill");
    const berthSelect = card.querySelector(".p-berth-select");
    
    nameInput?.addEventListener("input", (e) => {
      p.name = e.target.value.trim();
      if (p.name.length >= 2 && /^[a-zA-Z\s]+$/.test(p.name)) {
        nameInput.classList.remove("is-invalid");
        nameInput.classList.add("is-valid");
      } else {
        nameInput.classList.remove("is-valid");
      }
    });
    
    ageInput?.addEventListener("input", (e) => {
      const ageNum = parseInt(e.target.value);
      p.age = ageNum || "";
      if (ageNum >= 1 && ageNum <= 99) {
        ageInput.classList.remove("is-invalid");
        ageInput.classList.add("is-valid");
        
        if (ageNum >= 60) {
          p.isSenior = true;
          if (seniorCheck) seniorCheck.checked = true;
          if (seniorBadge) seniorBadge.style.display = "inline-block";
          if (berthSelect && p.berthPreference === "No Preference") {
            p.berthPreference = "Lower";
            berthSelect.value = "Lower";
          }
        }
      } else {
        ageInput.classList.remove("is-valid");
      }
    });
    
    genderPills.forEach(pill => {
      pill.addEventListener("click", () => {
        genderPills.forEach(g => g.classList.remove("active"));
        pill.classList.add("active");
        const rad = pill.querySelector("input");
        if (rad) {
          rad.checked = true;
          p.gender = rad.value;
        }
      });
    });
    
    berthSelect?.addEventListener("change", (e) => {
      p.berthPreference = e.target.value;
    });
    
    seniorCheck?.addEventListener("change", (e) => {
      p.isSenior = e.target.checked;
      if (seniorBadge) {
        seniorBadge.style.display = p.isSenior ? "inline-block" : "none";
      }
    });
    
    container.appendChild(card);
  });
}

function validatePassengers() {
  let allValid = true;
  let firstErrorEl = null;
  
  appState.passengersList.forEach((p) => {
    const card = document.querySelector(`.passenger-card[data-passenger-id="${p.id}"]`);
    if (!card) return;
    
    const nameInput = card.querySelector(".p-name-input");
    const ageInput = card.querySelector(".p-age-input");
    
    if (!p.name || p.name.length < 2 || !/^[a-zA-Z\s]+$/.test(p.name)) {
      allValid = false;
      nameInput.classList.add("is-invalid");
      if (!firstErrorEl) firstErrorEl = nameInput;
    } else {
      nameInput.classList.remove("is-invalid");
      nameInput.classList.add("is-valid");
    }
    
    const ageNum = parseInt(p.age);
    if (!ageNum || ageNum < 1 || ageNum > 99) {
      allValid = false;
      ageInput.classList.add("is-invalid");
      if (!firstErrorEl) firstErrorEl = ageInput;
    } else {
      ageInput.classList.remove("is-invalid");
      ageInput.classList.add("is-valid");
    }
  });
  
  const mobileInput = document.getElementById("contact-mobile-input");
  if (mobileInput) {
    const mobileVal = mobileInput.value.trim();
    if (mobileVal.length !== 10) {
      allValid = false;
      mobileInput.classList.add("is-invalid");
      if (!firstErrorEl) firstErrorEl = mobileInput;
    } else {
      mobileInput.classList.remove("is-invalid");
      mobileInput.classList.add("is-valid");
    }
  }
  
  if (!allValid && firstErrorEl) {
    firstErrorEl.scrollIntoView({ behavior: "smooth", block: "center" });
    firstErrorEl.focus();
    showToast("Please correct the highlighted errors before continuing.", "⚠️");
  }
  
  return allValid;
}

function setupScreen4Listeners() {
  document.getElementById("btn-back-to-class")?.addEventListener("click", () => {
    showScreen(3);
  });
  
  const accordionHeader = document.getElementById("journey-summary-accordion-header");
  const accordionBody = document.getElementById("journey-summary-accordion-body");
  const accordionChevron = document.getElementById("accordion-chevron");
  
  accordionHeader?.addEventListener("click", () => {
    if (accordionBody) {
      const isClosed = accordionBody.style.display === "none";
      accordionBody.style.display = isClosed ? "grid" : "none";
      if (accordionChevron) accordionChevron.textContent = isClosed ? "▲" : "▼";
    }
  });
  
  const mobileInput = document.getElementById("contact-mobile-input");
  mobileInput?.addEventListener("input", (e) => {
    const val = e.target.value.replace(/\D/g, "");
    e.target.value = val;
    appState.contact.mobile = val;
    if (val.length === 10) {
      mobileInput.classList.remove("is-invalid");
      mobileInput.classList.add("is-valid");
    } else {
      mobileInput.classList.remove("is-valid");
    }
  });
  
  document.getElementById("btn-continue-to-payment")?.addEventListener("click", () => {
    const isValid = validatePassengers();
    if (isValid) {
      openPassengerConfirmModal();
    }
  });
  
  document.getElementById("btn-confirm-proceed-pay")?.addEventListener("click", () => {
    document.getElementById("modal-passenger-confirm")?.classList.remove("open");
    proceedToPayment();
  });
}

function openPassengerConfirmModal() {
  const modal = document.getElementById("modal-passenger-confirm");
  const previewList = document.getElementById("confirm-passengers-preview-list");
  if (!modal || !previewList) return;
  
  let html = `
    <table style="width: 100%; border-collapse: collapse; font-size: 0.88rem;">
      <thead style="background: #f7faf8;">
        <tr>
          <th style="padding: 8px 12px; text-align: left; border-bottom: 1px solid var(--color-border);">#</th>
          <th style="padding: 8px 12px; text-align: left; border-bottom: 1px solid var(--color-border);">Full Name</th>
          <th style="padding: 8px 12px; text-align: left; border-bottom: 1px solid var(--color-border);">Age / Gender</th>
          <th style="padding: 8px 12px; text-align: left; border-bottom: 1px solid var(--color-border);">Berth Choice</th>
        </tr>
      </thead>
      <tbody>
  `;
  
  appState.passengersList.forEach(p => {
    html += `
      <tr>
        <td style="padding: 8px 12px; border-bottom: 1px solid #f0f4f1;">${p.id}</td>
        <td style="padding: 8px 12px; border-bottom: 1px solid #f0f4f1; font-weight: 700;">${p.name}</td>
        <td style="padding: 8px 12px; border-bottom: 1px solid #f0f4f1;">${p.age} yrs / ${p.gender}</td>
        <td style="padding: 8px 12px; border-bottom: 1px solid #f0f4f1;">${p.berthPreference}</td>
      </tr>
    `;
  });
  
  html += `</tbody></table>`;
  previewList.innerHTML = html;
  modal.classList.add("open");
}

// --- 11. Screen 5: Payment Processing ---
function proceedToPayment() {
  renderFareBreakdown();
  const failureBox = document.getElementById("payment-failure-box");
  if (failureBox) failureBox.style.display = "none";
  showScreen(5);
}

function renderFareBreakdown() {
  const count = appState.passengersCount;
  const basePerPerson = appState.selectedClass.effectiveFare;
  const baseTotal = basePerPerson * count;
  
  const isSuperfast = appState.selectedTrain.type === "Superfast";
  const superfastCharge = isSuperfast ? (45 * count) : 0;
  
  const isTatkal = appState.quota === "Tatkal" || appState.tatkalMode;
  const tatkalCharge = isTatkal ? (appState.selectedClass.code === "SL" ? 150 : 350) * count : 0;
  
  const isAC = ["3A", "2A", "1A", "CC"].includes(appState.selectedClass.code);
  const gst = isAC ? Math.round(baseTotal * 0.05) : 0;
  
  const resvFee = 40;
  const convenienceFee = 15;
  const total = baseTotal + superfastCharge + tatkalCharge + gst + resvFee + convenienceFee;
  
  appState.fareBreakdown = {
    baseFare: baseTotal,
    reservationFee: resvFee,
    superfastFee: superfastCharge,
    tatkalFee: tatkalCharge,
    gst: gst,
    convenienceFee: convenienceFee,
    total: total
  };
  
  const baseLabel = document.getElementById("fare-base-label");
  const baseVal = document.getElementById("fare-base-val");
  const sfRow = document.getElementById("fare-superfast-row");
  const tatkalRow = document.getElementById("fare-tatkal-row");
  const tatkalVal = document.getElementById("fare-tatkal-val");
  const gstVal = document.getElementById("fare-gst-val");
  const totalVal = document.getElementById("fare-total-val");
  const payBtnLabel = document.getElementById("pay-btn-label");
  
  if (baseLabel) baseLabel.textContent = `Base Fare: ${formatCurrency(basePerPerson)} × ${count} passenger${count > 1 ? 's' : ''}`;
  if (baseVal) baseVal.textContent = formatCurrency(baseTotal);
  
  if (sfRow) sfRow.style.display = isSuperfast ? "flex" : "none";
  if (tatkalRow) {
    tatkalRow.style.display = isTatkal ? "flex" : "none";
    if (tatkalVal) tatkalVal.textContent = formatCurrency(tatkalCharge);
  }
  
  if (gstVal) gstVal.textContent = formatCurrency(gst);
  if (totalVal) totalVal.textContent = formatCurrency(total);
  if (payBtnLabel) payBtnLabel.textContent = `Pay ${formatCurrency(total)}`;
}

function simulatePayment() {
  if (appState.isProcessingPayment) return;
  appState.isProcessingPayment = true;
  
  const payBtn = document.getElementById("btn-pay-now");
  if (payBtn) payBtn.disabled = true;
  
  const overlay = document.getElementById("payment-processing-overlay");
  const title = document.getElementById("processing-title");
  const status = document.getElementById("processing-status-text");
  
  if (overlay) overlay.style.display = "flex";
  if (title) title.textContent = "Processing your payment securely...";
  if (status) status.textContent = "Connecting with secure payment gateway...";
  
  setTimeout(() => {
    if (status) status.textContent = "Authenticating transaction with bank servers...";
  }, 1200);
  
  setTimeout(() => {
    if (overlay) overlay.style.display = "none";
    appState.isProcessingPayment = false;
    
    const failureCheckbox = document.getElementById("check-simulate-failure");
    let shouldFail = failureCheckbox ? failureCheckbox.checked : false;
    
    if (!shouldFail) {
      if (appState.paymentMethod === "upi") {
        shouldFail = (Math.random() > 0.85); // 85% success for UPI
      } else if (appState.paymentMethod === "card") {
        const cardNum = document.getElementById("card-number-input")?.value.replace(/\s/g, "");
        if (cardNum && cardNum.length > 0) {
          const lastDigit = parseInt(cardNum.slice(-1));
          shouldFail = (lastDigit % 2 !== 0); // odd fails, even succeeds
        }
      }
    }
    
    if (shouldFail) {
      if (payBtn) payBtn.disabled = false;
      const failureBox = document.getElementById("payment-failure-box");
      const txnIdEl = document.getElementById("failed-txn-id");
      if (txnIdEl) txnIdEl.textContent = "TXN_FAIL_" + Math.floor(10000000 + Math.random() * 90000000);
      if (failureBox) {
        failureBox.style.display = "block";
        failureBox.scrollIntoView({ behavior: "smooth", block: "start" });
      }
      showToast("Payment Failed. Your money has NOT been deducted.", "✕");
    } else {
      completeBooking();
    }
  }, 2500);
}

function setupScreen5Listeners() {
  document.getElementById("btn-back-to-passengers")?.addEventListener("click", () => {
    showScreen(4);
  });
  
  const payTabs = document.querySelectorAll(".pay-tab-btn");
  payTabs.forEach(tab => {
    tab.addEventListener("click", () => {
      payTabs.forEach(t => t.classList.remove("active"));
      tab.classList.add("active");
      
      const targetId = `paytab-${tab.getAttribute("data-paytab")}`;
      document.querySelectorAll(".pay-tab-content").forEach(c => c.classList.remove("active"));
      const content = document.getElementById(targetId);
      if (content) content.classList.add("active");
      appState.paymentMethod = tab.getAttribute("data-paytab");
    });
  });
  
  document.querySelectorAll(".upi-app-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".upi-app-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      appState.upiApp = btn.getAttribute("data-upiapp");
    });
  });
  
  document.getElementById("btn-verify-upi")?.addEventListener("click", () => {
    const input = document.getElementById("upi-id-input");
    const badge = document.getElementById("upi-verified-badge");
    if (!input || !badge) return;
    
    if (input.value.includes("@")) {
      badge.style.display = "block";
      showToast("UPI ID verified successfully!", "✓");
    } else {
      badge.style.display = "none";
      showToast("Please enter a valid UPI ID (e.g. name@bank)", "⚠️");
    }
  });
  
  const cardInput = document.getElementById("card-number-input");
  cardInput?.addEventListener("input", (e) => {
    let val = e.target.value.replace(/\D/g, "");
    val = val.substring(0, 16);
    const parts = [];
    for (let i = 0; i < val.length; i += 4) {
      parts.push(val.substring(i, i + 4));
    }
    e.target.value = parts.join(" ");
  });
  
  const expiryInput = document.getElementById("card-expiry-input");
  expiryInput?.addEventListener("input", (e) => {
    let val = e.target.value.replace(/\D/g, "");
    if (val.length >= 2) {
      val = val.substring(0, 2) + "/" + val.substring(2, 4);
    }
    e.target.value = val.substring(0, 5);
  });
  
  document.querySelectorAll(".bank-item-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".bank-item-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      appState.selectedBank = btn.getAttribute("data-bank");
    });
  });
  
  document.querySelectorAll(".wallet-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".wallet-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      appState.selectedWallet = btn.getAttribute("data-wallet");
    });
  });
  
  document.getElementById("btn-pay-now")?.addEventListener("click", simulatePayment);
  
  document.getElementById("btn-try-payment-again")?.addEventListener("click", () => {
    document.getElementById("payment-failure-box").style.display = "none";
    const payBtn = document.getElementById("btn-pay-now");
    if (payBtn) payBtn.disabled = false;
    const chk = document.getElementById("check-simulate-failure");
    if (chk) chk.checked = false;
    showToast("Ready for retry. Select payment method and proceed.", "ℹ️");
  });
  
  document.getElementById("btn-contact-support")?.addEventListener("click", () => {
    openHelpModal("safety");
  });
}

// --- 12. Screen 6: Confirmation & Ticket ---
function completeBooking() {
  appState.pnr = generatePNR();
  appState.transactionId = "TXN_" + new Date().toISOString().slice(0,10).replace(/-/g,"") + "_" + Math.floor(100000 + Math.random() * 900000);
  
  const now = new Date();
  appState.bookingTime = now.toLocaleDateString("en-IN", { day: "numeric", month: "short", year: "numeric" }) + " " + now.toLocaleTimeString("en-IN", { hour: "2-digit", minute: "2-digit" }) + " IST";
  
  appState.bookingStatus = (appState.selectedClass.status === "WL") ? "WAITLISTED" : (appState.selectedClass.status === "RAC" ? "RAC" : "CONFIRMED");
  
  const coachPrefix = appState.selectedClass.code === "3A" ? "B" : (appState.selectedClass.code === "2A" ? "A" : (appState.selectedClass.code === "1A" ? "H" : (appState.selectedClass.code === "CC" ? "C" : "S")));
  const coachNum = Math.floor(1 + Math.random() * 6);
  const coachCode = `${coachPrefix}${coachNum}`;
  
  const berthTypes = ["Lower", "Middle", "Upper", "Side Lower", "Side Upper"];
  let startSeat = Math.floor(12 + Math.random() * 40);
  
  appState.passengersList.forEach((p, idx) => {
    p.coach = (appState.bookingStatus === "WAITLISTED") ? "NA" : coachCode;
    p.seatNo = (appState.bookingStatus === "WAITLISTED") ? "NA" : (startSeat + idx);
    p.assignedBerthType = (appState.bookingStatus === "WAITLISTED") ? "Waitlisted" : (p.berthPreference !== "No Preference" ? p.berthPreference : berthTypes[idx % berthTypes.length]);
    p.ticketStatus = (appState.bookingStatus === "WAITLISTED") ? `WL-${34 + idx}` : (appState.bookingStatus === "RAC" ? `RAC-${2 + idx}` : "CNF / Confirmed");
  });
  
  const bookingRecord = {
    pnr: appState.pnr,
    txnId: appState.transactionId,
    train: appState.selectedTrain,
    class: appState.selectedClass,
    quota: appState.quota,
    journeyDate: appState.journeyDate,
    passengers: JSON.parse(JSON.stringify(appState.passengersList)),
    fare: appState.fareBreakdown.total,
    status: appState.bookingStatus,
    bookingTime: appState.bookingTime
  };
  
  appState.bookingsHistory.unshift(bookingRecord);
  updateBookingsBadge();
  saveBookingsToStorage();
  
  renderTicket(bookingRecord);
  showScreen(6);
  showToast("Booking Confirmed! 🎉", "✓");
}

function renderTicket(booking = appState.bookingsHistory[0]) {
  if (!booking) return;
  
  const pnrEl = document.getElementById("ticket-pnr-number");
  const timeEl = document.getElementById("ticket-booking-time");
  const txnEl = document.getElementById("ticket-txn-id");
  const bannerTitle = document.getElementById("confirmation-banner-title");
  const bannerSubtitle = document.getElementById("confirmation-banner-subtitle");
  
  if (pnrEl) pnrEl.textContent = booking.pnr;
  if (timeEl) timeEl.textContent = booking.bookingTime;
  if (txnEl) txnEl.textContent = booking.txnId;
  
  if (booking.status === "WAITLISTED") {
    if (bannerTitle) bannerTitle.textContent = translate("waitlistBanner");
    if (bannerSubtitle) bannerSubtitle.textContent = translate("waitlistSub");
  } else {
    if (bannerTitle) bannerTitle.textContent = translate("ticketConfirmedBanner");
    if (bannerSubtitle) bannerSubtitle.textContent = translate("ticketConfirmedSub");
  }
  
  const depTimeEl = document.getElementById("ticket-dep-time");
  const depCodeEl = document.getElementById("ticket-dep-code");
  const depNameEl = document.getElementById("ticket-dep-name");
  const journeyDateEl = document.getElementById("ticket-journey-date");
  
  const arrTimeEl = document.getElementById("ticket-arr-time");
  const arrCodeEl = document.getElementById("ticket-arr-code");
  const arrNameEl = document.getElementById("ticket-arr-name");
  const arrivalDateEl = document.getElementById("ticket-arrival-date");
  
  const trainFullEl = document.getElementById("ticket-train-fullname");
  const classQuotaEl = document.getElementById("ticket-class-quota-pill");
  const durationEl = document.getElementById("ticket-duration-val");
  const totalPaidEl = document.getElementById("ticket-fare-paid-val");
  
  if (depTimeEl) depTimeEl.textContent = booking.train.dep;
  if (depCodeEl) depCodeEl.textContent = appState.fromStation.code;
  if (depNameEl) depNameEl.textContent = getLocalizedStationName(appState.fromStation.code) || booking.train.originName;
  if (journeyDateEl) journeyDateEl.textContent = formatDate(booking.journeyDate);
  
  if (arrTimeEl) arrTimeEl.textContent = booking.train.arr.replace("+1", "");
  if (arrCodeEl) arrCodeEl.textContent = appState.toStation.code;
  if (arrNameEl) arrNameEl.textContent = getLocalizedStationName(appState.toStation.code) || booking.train.destName;
  if (arrivalDateEl) arrivalDateEl.textContent = formatDate(booking.journeyDate);
  
  if (trainFullEl) trainFullEl.textContent = `${booking.train.number} / ${getLocalizedTrainName(booking.train.name)}`;
  if (classQuotaEl) classQuotaEl.textContent = `${getLocalizedClassInfo(booking.class.code).fullName} (${booking.class.code}) · ${getLocalizedQuota(booking.quota)}`;
  if (durationEl) durationEl.textContent = `${booking.train.duration} · ${booking.train.distance || '701 km'}`;
  if (totalPaidEl) totalPaidEl.textContent = formatCurrency(booking.fare);
  
  const tbody = document.getElementById("ticket-passengers-tbody");
  if (tbody) {
    tbody.innerHTML = "";
    booking.passengers.forEach((p, idx) => {
      const row = document.createElement("tr");
      
      let statusBadge = "";
      if (p.ticketStatus.includes("CNF")) {
        statusBadge = `<span class="status-pill status-available">CNF</span>`;
      } else if (p.ticketStatus.includes("RAC")) {
        statusBadge = `<span class="status-pill status-rac">${p.ticketStatus}</span>`;
      } else {
        statusBadge = `<span class="status-pill status-wl">${p.ticketStatus}</span>`;
      }
      
      row.innerHTML = `
        <td>${idx + 1}</td>
        <td><strong>${p.name}</strong></td>
        <td>${p.age} / ${p.gender.charAt(0)}</td>
        <td><strong>${p.coach}</strong></td>
        <td><strong>${p.seatNo}</strong></td>
        <td>${getLocalizedBerthType(p.assignedBerthType)}</td>
        <td>${statusBadge}</td>
      `;
      tbody.appendChild(row);
    });
  }
}

function printTicket() {
  window.print();
}

function shareTicket() {
  const text = `My EasyRail Ticket: PNR ${appState.pnr} for ${appState.selectedTrain.name} (${appState.fromStation.code} -> ${appState.toStation.code}) on ${formatDate(appState.journeyDate)}. Status: ${appState.bookingStatus}`;
  if (navigator.share) {
    navigator.share({
      title: "EasyRail Train Ticket",
      text: text
    }).catch(() => {});
  } else {
    navigator.clipboard.writeText(text).then(() => {
      showToast("Journey details and PNR copied to clipboard!", "📋");
    });
  }
}

function setupScreen6Listeners() {
  document.getElementById("btn-print-ticket")?.addEventListener("click", printTicket);
  document.getElementById("btn-share-ticket")?.addEventListener("click", shareTicket);
  
  document.getElementById("btn-download-ticket")?.addEventListener("click", () => {
    const pnr = appState.pnr;
    const train = appState.selectedTrain;
    const ticketText = `
==================================================
           EASYRAIL ELECTRONIC TICKET
==================================================
PNR Number    : ${pnr}
Booking Status: ${appState.bookingStatus}
Train         : ${train.name} (${train.number})
Route         : ${appState.fromStation.code} -> ${appState.toStation.code}
Date          : ${formatDate(appState.journeyDate)}
Departure     : ${train.dep} | Arrival: ${train.arr}
Class         : ${appState.selectedClass.name} (${appState.selectedClass.code})
Total Fare    : ${formatCurrency(appState.fareBreakdown.total)}

PASSENGERS:
${appState.passengersList.map((p, i) => `${i+1}. ${p.name} (${p.age}/${p.gender}) - Coach: ${p.coach}, Seat: ${p.seatNo} (${p.assignedBerthType}) - Status: ${p.ticketStatus}`).join('\n')}

Important: Please carry a valid original government photo ID during journey.
==================================================
    `.trim();
    
    const blob = new Blob([ticketText], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `EasyRail_Ticket_${pnr}.txt`;
    link.click();
    URL.revokeObjectURL(url);
    showToast("Ticket downloaded as text file.", "📥");
  });
  
  document.getElementById("btn-copy-pnr")?.addEventListener("click", () => {
    navigator.clipboard.writeText(appState.pnr).then(() => {
      showToast(`PNR ${appState.pnr} copied to clipboard!`, "📋");
    });
  });
  
  document.getElementById("btn-translate-ticket")?.addEventListener("click", () => {
    // Cycle ticket language between English, Telugu, and Hindi
    const cycle = { en: "te", te: "hi", hi: "en" };
    const nextLang = cycle[appState.language] || "te";
    appState.language = nextLang;
    applyTranslations();
    const names = { en: "English", te: "తెలుగు (Telugu)", hi: "हिन्दी (Hindi)" };
    showToast(`Ticket translated to ${names[nextLang]} with Sarvam AI ✨`, "✨");
  });

  document.getElementById("btn-book-another")?.addEventListener("click", () => {
    appState.selectedTrain = null;
    appState.selectedClass = null;
    appState.passengersList = [];
    showScreen(1);
    showToast("Ready to plan your next journey!", "🚆");
  });
}

// --- 13. Modals & Drawer Management ---
function setupModalsAndDrawers() {
  document.querySelectorAll("[data-close-modal]").forEach(btn => {
    btn.addEventListener("click", () => {
      const modalId = btn.getAttribute("data-close-modal");
      document.getElementById(modalId)?.classList.remove("open");
    });
  });
  
  document.querySelectorAll(".modal-overlay").forEach(overlay => {
    overlay.addEventListener("click", (e) => {
      if (e.target === overlay) {
        overlay.classList.remove("open");
      }
    });
  });
  
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      document.querySelectorAll(".modal-overlay.open").forEach(m => m.classList.remove("open"));
      document.getElementById("bookings-drawer")?.classList.remove("open");
    }
  });
  
  document.getElementById("nav-help-btn")?.addEventListener("click", () => {
    openHelpModal("classes");
  });
  
  document.querySelectorAll(".help-modal-tab-btn").forEach(tab => {
    tab.addEventListener("click", () => {
      openHelpModal(tab.getAttribute("data-helptab"));
    });
  });
  
  document.getElementById("nav-bookings-btn")?.addEventListener("click", () => {
    renderBookingsDrawer();
    document.getElementById("bookings-drawer")?.classList.add("open");
  });
  
  document.getElementById("btn-close-bookings-drawer")?.addEventListener("click", () => {
    document.getElementById("bookings-drawer")?.classList.remove("open");
  });
}

function openHelpModal(tabKey = "classes") {
  const modal = document.getElementById("modal-help-guide");
  if (!modal) return;

  // --- Localized help content ---
  const helpContent = {
    en: {
      classes: {
        title: "Indian Railways Travel Classes Explained",
        items: [
          { label: "SL (Sleeper Class):", text: "Non-air-conditioned coach with open windows and 3-tier berths (Lower, Middle, Upper + Side Lower, Side Upper). Highly economical for long distance.", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "3A (AC 3 Tier):", text: "Air-conditioned coach with 3 berths on each side and 2 side berths. Blankets, bedsheets, and pillows are provided. Ideal balance of comfort and budget.", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "2A (AC 2 Tier):", text: "Air-conditioned coach with wider berths, only 2 berths per bay (Lower & Upper), reading lamps, and privacy curtains.", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "1A (AC First Class):", text: "Premium lockable private cabins (coupe with 2 berths or cabin with 4 berths). Includes full bedding and dedicated attendant service.", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "CC (AC Chair Car):", text: "Reclining push-back seats with 3×2 layout. Recommended for day journeys under 6 hours.", bg: "#f6faf7", border: "#d8ebd9" }
        ]
      },
      availability: {
        title: "What Do The Availability Codes Mean?",
        items: [
          { label: "AVAILABLE (CNF):", text: "Berths are readily available. You will be assigned a confirmed coach and berth number immediately upon payment.", bg: "#f0fdf4", border: "#bcf0cc", color: "var(--color-success)" },
          { label: "RAC (Reservation Against Cancellation):", text: "You are guaranteed a seat to travel on the train! Two RAC ticket holders share a side-lower berth. If confirmed passengers cancel, your ticket gets automatically upgraded to a full sleeper berth.", bg: "#fffbeb", border: "#fbe39d", color: "#b37905" },
          { label: "WL (Waitlist):", text: "No seat or berth is currently allotted. You cannot board the train on a waitlisted e-ticket. If seats become vacant before chart preparation, your ticket status advances to RAC or Confirmed.", bg: "#fef2f2", border: "#facfcf", color: "var(--color-error)" },
          { label: "GNWL vs PQWL vs RLWL:", text: "GNWL (General Waitlist) has the highest confirmation probability. PQWL (Pooled Quota) and RLWL (Remote Location) have lower confirmation priority.", bg: "#f8faf8", border: "#e1ebe3" }
        ]
      },
      tatkal: {
        title: "Everything You Need To Know About Tatkal",
        rows: [
          "⏰ <strong>Booking Opening Time:</strong> Tatkal booking opens exactly <strong>1 day prior</strong> to the train departure date from origin:<ul style='margin:6px 0 0 20px'><li><strong>10:00 AM:</strong> AC Classes (1A, 2A, 3A, CC, EC)</li><li><strong>11:00 AM:</strong> Non-AC Classes (SL, 2S)</li></ul>",
          "💰 <strong>Tatkal Charges:</strong> Fixed at 10% of basic fare for second class and 30% for all other classes (min ₹100, max ₹500).",
          "⚠️ <strong>Cancellation Policy:</strong> No refund is granted on cancellation of confirmed Tatkal tickets. Waitlisted Tatkal tickets are refunded automatically."
        ]
      },
      safety: {
        title: "Payment Security, Refunds & Rail Madad 139",
        rows: [
          "🔒 <strong>Safe Environment & Auto Refunds:</strong> 100% simulated refund for unconfirmed waitlist tickets after chart preparation.",
          "📞 <strong>Dial 139 (Rail Madad):</strong> 24×7 unified railway helpline in 12 languages.<br>• <strong>Press 1:</strong> Security & Medical assistance (connects to executive)<br>• <strong>Press 2:</strong> General/train enquiries (PNR, arrival/departure, fare, wheelchair)<br>• <strong>Press 4:</strong> General complaints<br>• <strong>Press *:</strong> Speak directly to call center executive",
          "👶 <strong>Other Channels:</strong> <strong>1098:</strong> Childline for lost/missing children · <strong>139 (SMS):</strong> SMS queries for PNR, AD, SPOT · <strong>Rail Madad App/Web:</strong> Online grievance tracking."
        ]
      }
    },
    hi: {
      classes: {
        title: "भारतीय रेलवे यात्रा श्रेणियाँ — विस्तृत जानकारी",
        items: [
          { label: "SL (स्लीपर क्लास):", text: "बिना वातानुकूलन वाला कोच जिसमें खुली खिड़कियाँ और 3-टियर बर्थ होती हैं (निचली, मध्य, ऊपरी + साइड लोअर, साइड अपर)। लंबी दूरी की किफायती यात्रा के लिए सर्वोत्तम।", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "3A (एसी 3 टियर):", text: "वातानुकूलित कोच जिसमें प्रत्येक साइड पर 3 और 2 साइड बर्थ होती हैं। चादर, कंबल और तकिया उपलब्ध कराए जाते हैं। आराम और बजट का सर्वश्रेष्ठ संयोजन।", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "2A (एसी 2 टियर):", text: "वातानुकूलित कोच जिसमें प्रति बे केवल 2 बर्थ (निचली और ऊपरी) होती हैं। चौड़े बर्थ, रीडिंग लैंप और गोपनीयता के लिए पर्दे दिए जाते हैं।", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "1A (एसी प्रथम श्रेणी):", text: "लॉक करने योग्य निजी केबिन — कूपे (2 बर्थ) या कैबिन (4 बर्थ)। पूर्ण बिस्तर सामग्री और समर्पित परिचारक सेवा उपलब्ध।", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "CC (एसी चेयर कार):", text: "3×2 लेआउट में पुश-बैक आरामदायक सीटें। 6 घंटे से कम की दिन की यात्राओं के लिए सबसे उपयुक्त।", bg: "#f6faf7", border: "#d8ebd9" }
        ]
      },
      availability: {
        title: "सीट उपलब्धता कोड का क्या अर्थ है?",
        items: [
          { label: "उपलब्ध (CNF):", text: "बर्थ तुरंत उपलब्ध है। भुगतान के बाद आपको तत्काल कन्फर्म कोच और बर्थ नंबर आवंटित किया जाएगा।", bg: "#f0fdf4", border: "#bcf0cc", color: "var(--color-success)" },
          { label: "RAC (रद्दीकरण के विरुद्ध आरक्षण):", text: "आपको ट्रेन में यात्रा की गारंटी मिलती है! दो RAC यात्री एक साइड लोअर बर्थ साझा करते हैं। यदि कन्फर्म यात्री टिकट रद्द करते हैं, तो आपका टिकट स्वतः पूर्ण बर्थ में अपग्रेड हो जाता है।", bg: "#fffbeb", border: "#fbe39d", color: "#b37905" },
          { label: "WL (वेटलिस्ट):", text: "अभी कोई सीट या बर्थ आवंटित नहीं हुई है। वेटलिस्ट ई-टिकट पर ट्रेन में बोर्ड नहीं किया जा सकता। चार्ट तैयार होने से पहले रद्दीकरण होने पर टिकट RAC या कन्फर्म हो सकता है।", bg: "#fef2f2", border: "#facfcf", color: "var(--color-error)" },
          { label: "GNWL बनाम PQWL बनाम RLWL:", text: "GNWL (सामान्य प्रतीक्षा सूची) की पुष्टि संभावना सबसे अधिक है। PQWL (पूल्ड कोटा) और RLWL (रिमोट लोकेशन) की प्राथमिकता कम होती है।", bg: "#f8faf8", border: "#e1ebe3" }
        ]
      },
      tatkal: {
        title: "तत्काल के बारे में सब कुछ जानें",
        rows: [
          "⏰ <strong>बुकिंग प्रारंभ समय:</strong> तत्काल बुकिंग ट्रेन के प्रस्थान से <strong>ठीक 1 दिन पहले</strong> खुलती है:<ul style='margin:6px 0 0 20px'><li><strong>सुबह 10:00 बजे:</strong> एसी श्रेणियाँ (1A, 2A, 3A, CC, EC)</li><li><strong>सुबह 11:00 बजे:</strong> गैर-एसी श्रेणियाँ (SL, 2S)</li></ul>",
          "💰 <strong>तत्काल शुल्क:</strong> सेकंड क्लास के लिए मूल किराये का 10% और अन्य सभी श्रेणियों के लिए 30% (न्यूनतम ₹100, अधिकतम ₹500)।",
          "⚠️ <strong>रद्दीकरण नीति:</strong> कन्फर्म तत्काल टिकट रद्द करने पर कोई रिफंड नहीं मिलता। वेटलिस्ट तत्काल टिकट स्वतः रिफंड हो जाते हैं।"
        ]
      },
      safety: {
        title: "भुगतान सुरक्षा, स्वतः रिफंड एवं रेल मदद 139",
        rows: [
          "🔒 <strong>सुरक्षित भुगतान एवं स्वतः रिफंड:</strong> अपुष्ट वेटलिस्ट टिकटों का 100% पूरा रिफंड चार्ट बनने के बाद सीधे मूल बैंक खाते में जमा हो जाता है।",
          "📞 <strong>डायल करें 139 (रेल मदद):</strong> 12 भाषाओं में 24 घंटे उपलब्ध एकीकृत यात्री हेल्पलाइन:<br>• <strong>1 दबाएं:</strong> सुरक्षा एवं आपात चिकित्सा सहायता (सीधे अधिकारी से बात)<br>• <strong>2 दबाएं:</strong> ट्रेन व पीएनआर पूछताछ (आगमन, प्रस्थान, किराया, व्हीलचेयर)<br>• <strong>4 दबाएं:</strong> सामान्य यात्री शिकायतें<br>• <strong>* दबाएं:</strong> सीधे कॉल सेंटर प्रतिनिधि से बात करें",
          "👶 <strong>अन्य हेल्पलाइन:</strong> <strong>1098:</strong> चाइल्डलाइन (गुमशुदा बच्चों की सहायता) · <strong>139 (SMS):</strong> PNR, SPOT, SEAT हेतु एसएमएस · <strong>रेल मदद ऐप/वेब:</strong> ऑनलाइन शिकायत दर्ज करें।"
        ]
      }
    },
    te: {
      classes: {
        title: "భారతీయ రైల్వే ప్రయాణ తరగతులు — వివరణ",
        items: [
          { label: "SL (స్లీపర్ క్లాస్):", text: "నాన్-ఏసీ కోచ్, తెరిచిన కిటికీలు మరియు 3-టైర్ బెర్తులు (దిగువ, మధ్య, పై + సైడ్ లోయర్, సైడ్ అప్పర్). సుదూర ప్రయాణానికి అత్యంత పొదుపైన ఎంపిక.", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "3A (ఏసీ 3 టైర్):", text: "ఎయిర్ కండిషన్డ్ కోచ్, ప్రతి వైపు 3 మరియు 2 సైడ్ బెర్తులు. దుప్పట్లు, బెడ్‌షీట్లు, దిండ్లు అందించబడతాయి. సౌకర్యం మరియు బడ్జెట్ యొక్క అత్యుత్తమ సమతుల్యం.", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "2A (ఏసీ 2 టైర్):", text: "ఎయిర్ కండిషన్డ్ కోచ్, బే కి కేవలం 2 బెర్తులు (దిగువ మరియు పై). విశాలమైన బెర్తులు, రీడింగ్ లైట్లు మరియు గోప్యత కోసం కర్టెన్లు.", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "1A (ఏసీ ఫస్ట్ క్లాస్):", text: "లాక్ చేయగలిగే ప్రైవేట్ క్యాబిన్లు — కూపే (2 బెర్తులు) లేదా క్యాబిన్ (4 బెర్తులు). పూర్తి బెడ్డింగ్ మరియు అంకితమైన అటెండెంట్ సేవతో అత్యుత్తమ ప్రయాణ అనుభవం.", bg: "#f6faf7", border: "#d8ebd9" },
          { label: "CC (ఏసీ చైర్ కార్):", text: "3×2 లేఅవుట్‌లో పుష్-బ్యాక్ సీట్లు. 6 గంటల లోపు పగటి ప్రయాణాలకు అత్యుత్తమం.", bg: "#f6faf7", border: "#d8ebd9" }
        ]
      },
      availability: {
        title: "సీట్ లభ్యత కోడ్‌ల అర్థం ఏమిటి?",
        items: [
          { label: "లభ్యం (CNF):", text: "బెర్తులు వెంటనే అందుబాటులో ఉన్నాయి. చెల్లింపు తర్వాత మీకు తక్షణమే కన్ఫర్మ్ కోచ్ మరియు బెర్త్ నంబర్ కేటాయించబడుతుంది.", bg: "#f0fdf4", border: "#bcf0cc", color: "var(--color-success)" },
          { label: "RAC (రద్దుకు వ్యతిరేకంగా రిజర్వేషన్):", text: "మీకు రైల్లో ప్రయాణించే హామీ ఉంది! ఇద్దరు RAC టికెట్ హోల్డర్లు ఒక సైడ్ లోయర్ బెర్త్‌ను పంచుకుంటారు. కన్ఫర్మ్ ప్రయాణికులు రద్దు చేస్తే, మీ టికెట్ స్వయంచాలకంగా పూర్తి బెర్త్‌కు అప్‌గ్రేడ్ అవుతుంది.", bg: "#fffbeb", border: "#fbe39d", color: "#b37905" },
          { label: "WL (వెయిట్‌లిస్ట్):", text: "ప్రస్తుతం సీటు లేదా బెర్త్ కేటాయించబడలేదు. వెయిట్‌లిస్ట్ ఈ-టికెట్‌పై రైల్లో ఎక్కడానికి అనుమతి లేదు. చార్ట్ తయారీకి ముందు రద్దులు జరిగితే స్థితి RAC లేదా కన్ఫర్మ్‌కు మారవచ్చు.", bg: "#fef2f2", border: "#facfcf", color: "var(--color-error)" },
          { label: "GNWL వర్సెస్ PQWL వర్సెస్ RLWL:", text: "GNWL (సాధారణ వెయిట్‌లిస్ట్)కు అత్యధిక నిర్ధారణ సంభావ్యత ఉంటుంది. PQWL (పూల్డ్ కోటా) మరియు RLWL (రిమోట్ లొకేషన్)కు తక్కువ ప్రాధాన్యత ఉంటుంది.", bg: "#f8faf8", border: "#e1ebe3" }
        ]
      },
      tatkal: {
        title: "తత్కాల్ గురించి మీకు తెలిసి ఉండవలసిన విషయాలు",
        rows: [
          "⏰ <strong>బుకింగ్ ప్రారంభ సమయం:</strong> తత్కాల్ బుకింగ్ రైలు బయల్దేరే <strong>ఒక రోజు ముందు</strong> మాత్రమే తెరుచుకుంటుంది:<ul style='margin:6px 0 0 20px'><li><strong>ఉదయం 10:00 గం.:</strong> ఏసీ తరగతులు (1A, 2A, 3A, CC, EC)</li><li><strong>ఉదయం 11:00 గం.:</strong> నాన్-ఏసీ తరగతులు (SL, 2S)</li></ul>",
          "💰 <strong>తత్కాల్ రుసుము:</strong> సెకండ్ క్లాస్‌కు మూల ధరలో 10%, ఇతర తరగతులకు 30% (కనీసం ₹100, గరిష్టం ₹500).",
          "⚠️ <strong>రద్దు విధానం:</strong> కన్ఫర్మ్ తత్కాల్ టికెట్ రద్దు చేస్తే రీఫండ్ ఇవ్వబడదు. వెయిట్‌లిస్ట్ తత్కాల్ టికెట్లు స్వయంచాలకంగా రీఫండ్ అవుతాయి."
        ]
      },
      safety: {
        title: "చెల్లింపు భద్రత, స్వయంచాలక రీఫండ్లు & రైల్ మదద్ 139",
        rows: [
          "🔒 <strong>సురక్షిత చెల్లింపులు & ఆటో-రీఫండ్:</strong> చార్ట్ తయారీ తర్వాత కన్ఫర్మ్ కాని టిక్కెట్లకు 100% రీఫండ్ తక్షణమే అసలు ఖాతాలో జమ అవుతుంది.",
          "📞 <strong>139 డయల్ చేయండి (రైల్ మదద్):</strong> 12 భాషలలో 24 గంటలూ అందుబాటులో ఉండే రైల్వే హెల్ప్‌లైన్:<br>• <strong>1 నొక్కండి:</strong> భద్రత మరియు అత్యవసర వైద్య సహాయం (ప్రత్యక్ష కనెక్షన్)<br>• <strong>2 నొక్కండి:</strong> రైలు & PNR విచారణలు (సమయాలు, ఛార్జీలు, వీల్‌చైర్)<br>• <strong>4 నొక్కండి:</strong> సాధారణ ప్రయాణీకుల ఫిర్యాదులు<br>• <strong>* నొక్కండి:</strong> కాల్ సెంటర్ ఎగ్జిక్యూటివ్‌తో నేరుగా మాట్లాడండి",
          "👶 <strong>ఇతర ఛానెల్‌లు:</strong> <strong>1098:</strong> చైల్డ్‌లైన్ (రక్షణ అవసరమైన పిల్లల సహాయం) · <strong>139 (SMS):</strong> PNR, SPOT సేవల కోసం SMS · <strong>రైల్ మదద్ యాప్/వెబ్:</strong> ఆన్‌లైన్ ఫిర్యాదు ట్రాకింగ్."
        ]
      }
    }
  };

  const lang = appState.language || "en";
  const data = helpContent[lang] || helpContent["en"];
  const tabData = data[tabKey] || data["classes"];
  const activeTabKey = tabKey in data ? tabKey : "classes";

  // Build panel HTML
  function makeItems(items) {
    return items.map(item => `
      <div style="padding:10px;background:${item.bg};border-radius:8px;border:1px solid ${item.border};">
        <strong${item.color ? ` style="color:${item.color}"` : ""}>${item.label}</strong> ${item.text}
      </div>`).join("");
  }
  function makeRows(rows) {
    return rows.map(r => `<div>${r}</div>`).join("");
  }

  let bodyHtml = `<h4 style="font-weight:800;margin-bottom:10px;">${tabData.title}</h4>`;
  if (activeTabKey === "safety") {
    bodyHtml += getSimplifiedRailMadadHtml(lang);
  } else if (tabData.items) {
    bodyHtml += `<div style="display:flex;flex-direction:column;gap:12px;font-size:0.9rem;line-height:1.5;">${makeItems(tabData.items)}</div>`;
  } else if (tabData.rows) {
    bodyHtml += `<div style="font-size:0.9rem;line-height:1.6;display:flex;flex-direction:column;gap:10px;">${makeRows(tabData.rows)}</div>`;
  }

  const container = document.getElementById("help-tab-content-container");
  if (container) container.innerHTML = bodyHtml;

  // Update tab button active state
  document.querySelectorAll(".help-modal-tab-btn").forEach(tab => {
    tab.classList.toggle("active", tab.getAttribute("data-helptab") === activeTabKey);
  });

  modal.classList.add("open");
}

function renderBookingsDrawer() {
  const container = document.getElementById("drawer-bookings-list");
  if (!container) return;
  
  if (appState.bookingsHistory.length === 0) {
    container.innerHTML = `
      <div class="empty-bookings-box">
        <div style="font-size: 2.5rem; margin-bottom: 12px;">🎫</div>
        <h4>No Bookings Yet</h4>
        <p style="font-size: 0.85rem; margin-top: 6px;">Your booked journey tickets will appear here for easy access and re-printing.</p>
      </div>
    `;
    return;
  }
  
  container.innerHTML = "";
  appState.bookingsHistory.forEach((item, idx) => {
    const card = document.createElement("div");
    card.className = `saved-booking-item ${item.status === 'CANCELLED' ? 'cancelled' : ''}`;
    
    card.innerHTML = `
      <div style="display: flex; align-items: center; justify-content: space-between;">
        <span style="font-size: 0.85rem; font-weight: 800; font-family: monospace; color: var(--color-primary);">PNR: ${item.pnr}</span>
        <span class="status-pill ${item.status === 'CANCELLED' ? 'status-wl' : 'status-available'}">${item.status}</span>
      </div>

      <div>
        <div style="font-weight: 800; font-size: 1rem;">${item.train.name} (${item.train.number})</div>
        <div style="font-size: 0.8rem; color: var(--color-muted);">${formatDate(item.journeyDate)} · ${item.class.code} · ${item.passengers.length} Passenger(s)</div>
      </div>

      <div style="font-size: 0.85rem; font-weight: 700; color: var(--color-text);">
        Paid: ${formatCurrency(item.fare)}
      </div>

      <div style="display: flex; gap: 8px; margin-top: 6px;">
        ${item.status === 'CANCELLED' ? `
          <button type="button" class="btn btn-outline btn-track-refund" data-index="${idx}" style="min-height: 34px; padding: 4px 14px; font-size: 0.82rem; color: #176B48; border-color: #176B48; font-weight: 700;">
            🔍 ${appState.language === 'hi' ? 'रिफंड स्थिति ट्रैक करें' : appState.language === 'te' ? 'రీఫండ్ స్థితిని ట్రాక్ చేయండి' : 'Track Refund Status'}
          </button>
        ` : `
          <button type="button" class="btn btn-primary btn-view-saved-ticket" data-index="${idx}" style="min-height: 34px; padding: 4px 12px; font-size: 0.82rem;">
            ${translate('viewTicket') || 'View Ticket'}
          </button>
          <button type="button" class="btn btn-outline btn-cancel-saved-ticket" data-index="${idx}" style="min-height: 34px; padding: 4px 12px; font-size: 0.82rem; color: var(--color-error);">
            ${translate('cancelBooking') || 'Cancel Booking'}
          </button>
        `}
      </div>
    `;
    
    card.querySelector(".btn-view-saved-ticket")?.addEventListener("click", () => {
      document.getElementById("bookings-drawer")?.classList.remove("open");
      renderTicket(item);
      showScreen(6);
    });

    card.querySelector(".btn-track-refund")?.addEventListener("click", () => {
      openRefundTrackerModal(item);
    });
    
    card.querySelector(".btn-cancel-saved-ticket")?.addEventListener("click", () => {
      if (confirm(`Are you sure you want to cancel ticket with PNR ${item.pnr}? A simulated refund of ${formatCurrency(item.fare - 60)} will be credited.`)) {
        item.status = "CANCELLED";
        item.cancelledAt = new Date().toISOString();
        item.refundAmount = Math.max(0, item.fare - 60);
        item.refundStatus = "REFUNDED_TO_SOURCE";
        item.bankArn = "IRCTC" + (item.pnr || "1234567890").replace(/[^0-9]/g, "") + "BNK";
        saveBookingsToStorage();
        renderBookingsDrawer();
        openRefundTrackerModal(item);
        showToast(`Ticket cancelled. Simulated refund of ${formatCurrency(item.fare - 60)} credited.`, "ℹ️");
      }
    });
    
    container.appendChild(card);
  });
}

function openRefundTrackerModal(item) {
  const modal = document.getElementById("modal-refund-status");
  const body = document.getElementById("refund-modal-body");
  if (!modal || !body) return;
  
  const refundAmt = Math.max(0, (item.fare || 1000) - 60);
  const lang = appState.language;
  const arnNumber = item.bankArn || `IRCTC${(item.pnr || '1234567890').replace(/[^0-9]/g, '')}BNK`;
  
  let cancelApprovedText = "Cancellation Approved & Processed";
  let refundApprovedNotice = "This ticket has been cancelled in the railway reservation system. Berths have been released back to waitlisted passengers. No travel is permitted on this PNR.";
  let totalFareText = "Total Fare Paid";
  let cancelFeeText = "IRCTC Cancellation Fee";
  let netRefundText = "Net Refund Amount";
  let refundDestText = "Refund Destination";
  let refundDestVal = "Source Bank Account (Simulated UPI/NetBanking)";
  let refArnText = "Bank Reference / ARN";
  let step1Title = "Cancellation Approved";
  let step1Desc = "Instant cancellation request approved by IRCTC reservation engine.";
  let step2Title = "Refund Initiated by IRCTC";
  let step2Desc = "Refund payment batch generated and transferred to acquiring bank.";
  let step3Title = "Credited to Bank Account";
  let step3Desc = `Amount of ${formatCurrency(refundAmt)} successfully credited back to original payment mode.`;
  
  if (lang === "hi") {
    cancelApprovedText = "रद्दीकरण स्वीकृत एवं पूर्ण";
    refundApprovedNotice = "यह टिकट रेलवे आरक्षण प्रणाली में रद्द कर दिया गया है। सीट/बर्थ अन्य यात्रियों को आवंटित कर दी गई है। इस पीएनआर पर यात्रा की अनुमति नहीं है।";
    totalFareText = "कुल भुगतान किया गया किराया";
    cancelFeeText = "आईआरसीटीसी रद्दीकरण शुल्क";
    netRefundText = "शुद्ध रिफंड राशि";
    refundDestText = "रिफंड गंतव्य";
    refundDestVal = "मूल बैंक खाता / यूपीआई";
    refArnText = "बैंक संदर्भ संख्या (ARN)";
    step1Title = "रद्दीकरण स्वीकृत";
    step1Desc = "आईआरसीटीसी द्वारा टिकट रद्दीकरण तुरंत अनुमोदित किया गया।";
    step2Title = "रिफंड प्रक्रिया प्रारंभ";
    step2Desc = "रिफंड बैच तैयार कर पेमेंट गेटवे को हस्तांतरित किया गया।";
    step3Title = "बैंक खाते में जमा";
    step3Desc = `${formatCurrency(refundAmt)} की राशि मूल भुगतान विधि में सफलतापूर्वक जमा कर दी गई है।`;
  } else if (lang === "te") {
    cancelApprovedText = "రద్దు ఆమోదించబడింది & పూర్తి చేయబడింది";
    refundApprovedNotice = "ఈ టిక్కెట్ రైల్వే రిజర్వేషన్ వ్యవస్థలో రద్దు చేయబడింది. బెర్తులు ఇతర ప్రయాణీకులకు కేటాయించబడ్డాయి. ఈ PNRతో ప్రయాణం అనుమతించబడదు.";
    totalFareText = "చెల్లించిన మొత్తం ఛార్జీ";
    cancelFeeText = "IRCTC రద్దు రుసుము";
    netRefundText = "నికర రీఫండ్ మొత్తం";
    refundDestText = "రీఫండ్ జమ అయ్యే ఖాతా";
    refundDestVal = "అసలు బ్యాంక్ ఖాతా / UPI";
    refArnText = "బ్యాంక్ రిఫరెన్స్ (ARN)";
    step1Title = "రద్దు ఆమోదం పొందింది";
    step1Desc = "IRCTC ద్వారా టికెట్ రద్దు అభ్యర్థన తక్షణమే ఆమోదించబడింది.";
    step2Title = "రీఫండ్ ప్రారంభించబడింది";
    step2Desc = "రీఫండ్ బ్యాచ్ ప్రాసెస్ చేయబడి పేమెంట్ గేట్‌వేకి పంపబడింది.";
    step3Title = "బ్యాంక్ ఖాతాలో జమ చేయబడింది";
    step3Desc = `${formatCurrency(refundAmt)} మొత్తం మీ అసలు చెల్లింపు విధానానికి విజయవంతంగా జమ చేయబడింది.`;
  }
  
  body.innerHTML = `
    <div class="refund-tracker-card">
      <div class="refund-status-badge-row">
        <span style="color: var(--color-error); font-size: 0.95rem;">🔴 ${cancelApprovedText}</span>
        <span style="font-family: monospace; font-size: 0.85rem; color: var(--color-muted);">PNR: ${item.pnr}</span>
      </div>

      <div style="font-size: 0.85rem; background: #fff8f8; padding: 10px 12px; border-radius: 8px; border: 1px solid #ffd6d6; color: #991b1b; line-height: 1.45;">
        ⚠️ <strong>${refundApprovedNotice}</strong>
      </div>

      <div class="refund-breakdown-box">
        <div class="refund-breakdown-row">
          <span>${totalFareText}:</span>
          <strong>${formatCurrency(item.fare)}</strong>
        </div>
        <div class="refund-breakdown-row" style="color: var(--color-muted);">
          <span>${cancelFeeText}:</span>
          <span>- ₹60</span>
        </div>
        <div class="refund-breakdown-row" style="font-size: 1rem; font-weight: 800; color: var(--color-primary); border-top: 1px dashed #d0e4d6; padding-top: 8px;">
          <span>${netRefundText}:</span>
          <span>${formatCurrency(refundAmt)}</span>
        </div>
      </div>

      <div style="display: flex; flex-direction: column; gap: 4px; font-size: 0.82rem; background: #f0f7f3; padding: 10px 12px; border-radius: 8px; border: 1px solid #cce5d6;">
        <div><strong>${refundDestText}:</strong> ${refundDestVal}</div>
        <div><strong>${refArnText}:</strong> <code style="font-family: monospace; font-weight: 700;">${arnNumber}</code></div>
      </div>

      <div style="font-weight: 800; font-size: 0.92rem; margin-top: 4px; color: var(--color-text);">
        📊 Live Refund Timeline
      </div>

      <div class="refund-timeline">
        <div class="refund-step">
          <div class="refund-step-dot">✓</div>
          <div class="refund-step-title">${step1Title}</div>
          <div class="refund-step-desc">${step1Desc}</div>
        </div>
        <div class="refund-step">
          <div class="refund-step-dot">✓</div>
          <div class="refund-step-title">${step2Title}</div>
          <div class="refund-step-desc">${step2Desc}</div>
        </div>
        <div class="refund-step">
          <div class="refund-step-dot">✓</div>
          <div class="refund-step-title" style="color: var(--color-success); font-weight: 800;">${step3Title} ✅</div>
          <div class="refund-step-desc" style="color: #176B48; font-weight: 600;">${step3Desc}</div>
        </div>
      </div>
    </div>
  `;
  
  modal.classList.add("open");
}

function updateBookingsBadge() {
  const badge = document.getElementById("bookings-count-badge");
  if (badge) {
    badge.textContent = appState.bookingsHistory.length;
  }
}

function saveBookingsToStorage() {
  try {
    localStorage.setItem("easyrail_bookings", JSON.stringify(appState.bookingsHistory));
  } catch (e) {}
}

function loadBookingsFromStorage() {
  try {
    const raw = localStorage.getItem("easyrail_bookings");
    if (raw) {
      appState.bookingsHistory = JSON.parse(raw);
      updateBookingsBadge();
    }
  } catch (e) {}
}

// --- 14. Header & Accessibility Mode ---
function setupHeaderAndA11y() {
  document.getElementById("header-brand-logo")?.addEventListener("click", (e) => {
    e.preventDefault();
    showScreen(1);
  });
  
  document.getElementById("nav-home-btn")?.addEventListener("click", () => {
    showScreen(1);
  });
  
  const a11yBtn = document.getElementById("a11y-toggle-btn");
  const a11yBannerClose = document.getElementById("a11y-banner-close");
  
  function toggleA11y() {
    appState.accessibilityMode = !appState.accessibilityMode;
    document.body.classList.toggle("accessibility-mode", appState.accessibilityMode);
    if (a11yBtn) a11yBtn.setAttribute("aria-pressed", appState.accessibilityMode);
    
    if (appState.accessibilityMode) {
      showToast("Accessibility mode ON: Larger text & high contrast.", "♿");
    } else {
      showToast("Accessibility mode OFF.", "ℹ️");
    }
  }
  
  a11yBtn?.addEventListener("click", toggleA11y);
  a11yBannerClose?.addEventListener("click", toggleA11y);
  
  const langTrigger = document.getElementById("lang-menu-trigger");
  const langMenu = document.getElementById("lang-dropdown-menu");
  
  langTrigger?.addEventListener("click", (e) => {
    e.stopPropagation();
    langMenu?.classList.toggle("open");
  });
  
  document.querySelectorAll("#lang-dropdown-menu button[data-lang]").forEach(btn => {
    btn.addEventListener("click", () => {
      const selectedLang = btn.getAttribute("data-lang");
      if (!selectedLang) return;
      appState.language = selectedLang;
      
      document.querySelectorAll("#lang-dropdown-menu button[data-lang]").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      
      applyTranslations();
      langMenu?.classList.remove("open");
      
      const langNames = { en: "English", hi: "हिन्दी", te: "తెలుగు" };
      showToast(`Language set to ${langNames[selectedLang]}`, "🌐");
    });
  });
  
  document.addEventListener("click", (e) => {
    if (langMenu && !langTrigger.contains(e.target) && !langMenu.contains(e.target)) {
      langMenu.classList.remove("open");
    }
  });

  document.getElementById("nav-sarvam-btn")?.addEventListener("click", () => {
    openSarvamStudioModal();
  });

  document.getElementById("menu-open-sarvam-studio")?.addEventListener("click", () => {
    langMenu?.classList.remove("open");
    openSarvamStudioModal();
  });
}

// --- 15. Sarvam AI Deep Translate Studio Controllers ---
function openSarvamStudioModal(preloadedText = null, targetLang = null) {
  const modal = document.getElementById("modal-sarvam-translate");
  if (!modal) return;
  modal.style.display = "flex";
  modal.classList.add("open");

  if (targetLang) {
    const tgtSelect = document.getElementById("sarvam-target-lang");
    if (tgtSelect) tgtSelect.value = targetLang;
  }

  const inputEl = document.getElementById("sarvam-input-text");
  if (preloadedText && inputEl) {
    inputEl.value = preloadedText;
    updateSarvamCharCount();
    performStudioTranslation();
  } else if (inputEl && !inputEl.value.trim()) {
    inputEl.value = "Your train 12626 Kerala Express is running on time. Arriving at Platform 3. Coach B2, Berth 34 (Lower).";
    updateSarvamCharCount();
    performStudioTranslation();
  }

  const keyInput = document.getElementById("sarvam-api-key-input");
  if (keyInput) {
    keyInput.value = SarvamAI.getApiKey();
  }
  SarvamAI.updateStatusBadge();
}

function closeSarvamStudioModal() {
  const modal = document.getElementById("modal-sarvam-translate");
  if (modal) {
    modal.classList.remove("open");
    modal.style.display = "none";
  }
}

function updateSarvamCharCount() {
  const inputEl = document.getElementById("sarvam-input-text");
  const countEl = document.getElementById("sarvam-char-count");
  if (inputEl && countEl) {
    countEl.textContent = `${inputEl.value.length} / 2,000 chars`;
  }
}

async function performStudioTranslation() {
  const inputEl = document.getElementById("sarvam-input-text");
  const outputEl = document.getElementById("sarvam-output-text");
  const srcSelect = document.getElementById("sarvam-source-lang");
  const tgtSelect = document.getElementById("sarvam-target-lang");
  const modeSelect = document.getElementById("sarvam-mode-select");
  const genderSelect = document.getElementById("sarvam-gender-select");
  const numeralsSelect = document.getElementById("sarvam-numerals-select");
  const translateBtn = document.getElementById("sarvam-translate-action-btn");

  if (!inputEl || !outputEl) return;
  const text = inputEl.value.trim();
  if (!text) {
    outputEl.textContent = "Please enter or paste text to translate.";
    return;
  }

  const srcLang = srcSelect ? srcSelect.value : "auto";
  const tgtLang = tgtSelect ? tgtSelect.value : "te-IN";
  const mode = modeSelect ? modeSelect.value : "formal";
  const gender = genderSelect ? genderSelect.value : "None";
  const numerals = numeralsSelect ? numeralsSelect.value : "international";

  if (translateBtn) {
    translateBtn.disabled = true;
    translateBtn.textContent = "Translating with Sarvam AI...";
  }
  outputEl.textContent = "Performing deep context-aware translation...";

  try {
    const translated = await SarvamAI.translate({
      input: text,
      sourceLang: srcLang,
      targetLang: tgtLang,
      mode: mode,
      speakerGender: gender,
      numeralsFormat: numerals
    });

    outputEl.textContent = translated;
  } catch (err) {
    outputEl.textContent = "Translation error: " + err.message;
  } finally {
    if (translateBtn) {
      translateBtn.disabled = false;
      translateBtn.textContent = "✨ Translate with Sarvam AI";
    }
  }
}

function setupSarvamDeepTranslateStudio() {
  document.getElementById("btn-close-sarvam-modal")?.addEventListener("click", closeSarvamStudioModal);
  document.getElementById("btn-done-sarvam-modal")?.addEventListener("click", closeSarvamStudioModal);
  document.getElementById("modal-sarvam-translate")?.addEventListener("click", (e) => {
    if (e.target.id === "modal-sarvam-translate") {
      closeSarvamStudioModal();
    }
  });

  document.getElementById("sarvam-swap-langs-btn")?.addEventListener("click", () => {
    const srcSelect = document.getElementById("sarvam-source-lang");
    const tgtSelect = document.getElementById("sarvam-target-lang");
    if (!srcSelect || !tgtSelect) return;

    let curSrc = srcSelect.value === "auto" ? "en-IN" : srcSelect.value;
    let curTgt = tgtSelect.value;

    srcSelect.value = curTgt;
    tgtSelect.value = curSrc;

    const inputEl = document.getElementById("sarvam-input-text");
    const outputEl = document.getElementById("sarvam-output-text");
    if (inputEl && outputEl && outputEl.textContent && !outputEl.textContent.startsWith("Please") && !outputEl.textContent.startsWith("Performing")) {
      inputEl.value = outputEl.textContent;
      updateSarvamCharCount();
      performStudioTranslation();
    }
  });

  document.getElementById("sarvam-source-lang")?.addEventListener("change", performStudioTranslation);
  document.getElementById("sarvam-target-lang")?.addEventListener("change", performStudioTranslation);
  document.getElementById("sarvam-mode-select")?.addEventListener("change", performStudioTranslation);
  document.getElementById("sarvam-gender-select")?.addEventListener("change", performStudioTranslation);
  document.getElementById("sarvam-numerals-select")?.addEventListener("change", performStudioTranslation);

  const inputEl = document.getElementById("sarvam-input-text");
  inputEl?.addEventListener("input", updateSarvamCharCount);

  document.getElementById("sarvam-clear-input-btn")?.addEventListener("click", () => {
    if (inputEl) {
      inputEl.value = "";
      updateSarvamCharCount();
      inputEl.focus();
    }
    const outputEl = document.getElementById("sarvam-output-text");
    if (outputEl) outputEl.textContent = "";
  });

  document.getElementById("sarvam-translate-action-btn")?.addEventListener("click", performStudioTranslation);

  const presets = {
    status: "Your train 12626 Kerala Express is running on time. Arriving at Platform 3. Coach B2, Berth 34 (Lower).",
    tatkal: "Tatkal quota tickets open exactly 1 day prior to departure at 10:00 AM (AC) and 11:00 AM (Non-AC). No refund on cancellation of confirmed Tatkal tickets.",
    rac: "RAC guarantees a travel seat on the train. Waitlist (WL) does not allot a berth yet; it upgrades to RAC or Confirmed if cancellations occur before charting.",
    senior: "Male passengers aged 60+ and solo female passengers aged 45+ are automatically given lower berth priority as per Indian Railways quota rules.",
    safety: "Indian Railways operates the 24x7 unified passenger emergency helpline 139 for security, medical help, and real-time train status."
  };

  document.querySelectorAll(".sarvam-preset-chip").forEach(chip => {
    chip.addEventListener("click", () => {
      const presetKey = chip.getAttribute("data-preset");
      if (presets[presetKey] && inputEl) {
        inputEl.value = presets[presetKey];
        updateSarvamCharCount();
        performStudioTranslation();
      }
    });
  });

  document.getElementById("sarvam-copy-output-btn")?.addEventListener("click", () => {
    const outputEl = document.getElementById("sarvam-output-text");
    if (!outputEl || !outputEl.textContent.trim()) return;
    navigator.clipboard.writeText(outputEl.textContent.trim()).then(() => {
      showToast("Translation copied to clipboard! 📋", "✓");
    });
  });

  document.getElementById("sarvam-speak-output-btn")?.addEventListener("click", () => {
    const outputEl = document.getElementById("sarvam-output-text");
    const tgtSelect = document.getElementById("sarvam-target-lang");
    if (!outputEl || !outputEl.textContent.trim() || !window.speechSynthesis) return;

    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(outputEl.textContent.trim());
    const langCode = tgtSelect ? tgtSelect.value : "te-IN";
    utterance.lang = langCode;
    utterance.rate = 0.95;
    window.speechSynthesis.speak(utterance);
    showToast("Speaking translation... 🔊", "🔊");
  });

  document.getElementById("sarvam-apply-page-btn")?.addEventListener("click", () => {
    const tgtSelect = document.getElementById("sarvam-target-lang");
    const fullCode = tgtSelect ? tgtSelect.value : "te-IN";
    const shortCode = fullCode.split("-")[0];
    appState.language = shortCode;
    applyTranslations();
    closeSarvamStudioModal();
    const names = { en: "English", te: "తెలుగు (Telugu)", hi: "हिन्दी (Hindi)" };
    showToast(`App language set to ${names[shortCode]} using Sarvam AI ✨`, "🌐");
  });

  document.getElementById("sarvam-save-key-btn")?.addEventListener("click", () => {
    const keyInput = document.getElementById("sarvam-api-key-input");
    if (!keyInput) return;
    const val = keyInput.value.trim();
    SarvamAI.setApiKey(val);
    if (val) {
      showToast("Sarvam AI subscription key saved! Live cloud calls enabled.", "✓");
    } else {
      showToast("Sarvam AI key removed. Using context engine.", "ℹ️");
    }
  });

  document.getElementById("sarvam-clear-key-btn")?.addEventListener("click", () => {
    const keyInput = document.getElementById("sarvam-api-key-input");
    if (keyInput) keyInput.value = "";
    SarvamAI.setApiKey("");
    showToast("Sarvam AI key removed.", "ℹ️");
  });
}

// --- 16. DOM Ready Bootstrap ---
document.addEventListener("DOMContentLoaded", () => {
  // Restore language preference saved from last session
  const savedLang = (() => { try { return localStorage.getItem("easyrail_lang"); } catch(e) { return null; } })();
  if (savedLang && ["en","hi","te"].includes(savedLang)) {
    appState.language = savedLang;
  }
  SarvamAI.init();
  initSearch();
  setupScreen2Listeners();
  setupScreen3Listeners();
  setupScreen4Listeners();
  setupScreen5Listeners();
  setupScreen6Listeners();
  setupModalsAndDrawers();
  setupHeaderAndA11y();
  setupSarvamDeepTranslateStudio();
  loadBookingsFromStorage();
  applyTranslations();
  
  showScreen(1);
});
"""
