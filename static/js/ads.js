// Setup
function setup(){
  getAccounts();
  // Only show the accounts list.
  $(".ads-accounts").show();
  $(".ads-campaigns").hide();
  $(".ads-lineitems").hide();
  $(".ads-targeting").hide();
}
// get the accountList
function getAccounts(){
  $.getJSON("../ads/api/accounts",
  function (json) {
    localStorage.setItem("adsAccounts", JSON.stringify(json["accounts"]));
  });
}

setup();

function listAccounts(){
  var accountList = JSON.parse(localStorage.getItem("adsAccounts"))
  $(accountList).each(function( index ) {
    $(".dropdown-ads-accounts").append("<li><a href='#' class='ads-api-account' data-id='" + accountList[index].id + "'>" + accountList[index].name + "</a></li>");
  });
  // onclick Item
  $(".ads-api-account").click(function(e) {
    e.preventDefault();
    var accountId = $(this).data("id");
    getCampaigns(accountId)
    // remove Ads Tools
    $(".ads-accounts").hide();
    $(".ads-api-account").remove();
    // Setup Campaigns
    $(".ads-campaigns").show();
    getCampaigns();
  });
}

// get the campaignList
function getCampaigns(account_id){
  $.getJSON("../ads/api/campaigns?account_id=" + account_id,
  function (json) {
    $(json["campaigns"]).each(function( index ) {
      var campaign = json["campaigns"][index]
      $(".dropdown-ads-campaigns").append("<li><a href='#' class='ads-api-campaign' data-id='" + campaign.id + "'>" + campaign.name + "</a></li>");
    });
    // onclick Item
    $(".ads-api-campaign").click(function(e) {
      e.preventDefault();
      var campaign_id = $(this).data("id");
      getLineItems(account_id, campaign_id);
      // Remove Campaign
      $(".ads-campaigns").hide();
      $(".ads-api-campaign").remove();
      // Setup Campaigns
      $(".ads-lineitems").show();
    });
  });
}

// get the lineItems
function getLineItems(account_id, campaign_id){
  $.getJSON("../ads/api/line_items?account_id=" + account_id + "&campaign_id=" + campaign_id,
  function (json) {

    $(json["line_items"]).each(function( index ) {
      var lineItem = json["line_items"][index];
      $(".dropdown-ads-lineitems").append("<li><a href='#' class='ads-api-lineitem' data-id='" + lineItem.id + "'>" + lineItem.name + "</a></li>");
    });
    // LineItem
    $(".ads-api-lineitem").click(function(e) {
      localStorage.setItem("line_item", $(this).data("id"))
      $(".ads-lineitems").hide();
      $(".ads-api-lineitem").remove();
      $(".ads-targeting").show();
      getTargetingCriteria(account_id, campaign_id, $(this).data("id"));
    });
  });
}



function getTargetingCriteria(account_id, campaign_id, line_item_id){
  $(".ads-add-targeting").click(function(e) {
    setTargetingCriteria(account_id, campaign_id, line_item_id);
  });

  var checkedVals = $('.term:checkbox:checked').map(function() {
    return this.value;
  }).get();


  $(checkedVals).each(function( index ) {
    console.log(checkedVals);
    $(".ads-targeting-list").append("<li>" + checkedVals[index] + "</li>");
  });

}

// set TargetingCriteria
function setTargetingCriteria(account_id, campaign_id, line_item_id){
  //
  var checkedVals = $('.term:checkbox:checked').map(function() {
    return this.value;
  }).get();

  // for each value send http request to create a targeting criteria
  $(checkedVals).each(function( index ) {
    var targeting_value = checkedVals[index];
    $.getJSON("../../ads/api/targeting/new?account_id=" + account_id + "&line_item_id=" + campaign_id + "&targeting_value=" + targeting_value,
    function (json) {
      console.log(json);
    });
  });
}

// Ads-Modal on close
$('#adsModal').on('shown.bs.modal', function () {
  setup();
})
